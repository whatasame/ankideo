import os
from abc import abstractmethod
from typing import Set, List

from aqt.editor import Editor

from ..constants.convert_video_key import ConvertVideoFieldsKey
from ..constants.embed_media_key import EmbedMediaFieldsKey
from ..constants.extract_audio_key import ExtractAudioFieldsKey
from ..constants.json_key import JsonKey
from ..core.config import Config
from ..core.exception import AnkidiaError
from ..core.old_constants import FieldKey
from ..core.utils import to_abs_path, to_sound_tag
from ..embed.html_media_embedder import HtmlMediaEmbedder
from ..ffmpeg.commands import ConvertVideoFFmpegCommand, ExtractAudioFFmpegCommand, Mp4FFmpegCommand, WebmFFmpegCommand
from ..ffmpeg.worker import FFmpegManager
from ..service.whisper_service import speech_to_text


class EditorButton:
    def __init__(self, allowed_field_keys: Set[JsonKey], icon_path: str, cmd: str, tip: str):
        self.field_keys = allowed_field_keys
        self.icon_path = icon_path
        self.cmd = cmd
        self.tip = tip
        self.config = Config()

    def on_click(self, editor: Editor):
        self._validate_field(editor)

        self.config = Config()  # Refresh config

        self.operate(editor)

    def _redraw_note(self, editor):
        """
        If you want to redraw note after click, you should give them a callback function
        including redraw function. Because asynchronous operation results after operate function ends.

        And see more below why this function is needed.
        https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
        """
        editor.set_note(editor.note)

    def _validate_field(self, editor):
        """
        Validate if the fields are existed in the note
        """
        for field_key in self.field_keys:
            field_name = self.config[field_key]

            if not field_name in editor.note:
                raise AnkidiaError(f"Field '{field_name}' doesn't exist in the note.")

    @abstractmethod
    def operate(self, editor):
        pass

    def _get_selected_field_name(self, editor: Editor) -> str:
        """
        :return: Returns the name of the current selected field that cursor is on in the editor
        """
        current_field_index = editor.currentField
        if current_field_index is None:
            raise AnkidiaError("Click media field to embed")

        current_field_name = editor.note.keys()[current_field_index]

        return current_field_name


class ConvertVideoFormatButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={ConvertVideoFieldsKey.VIDEO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "convert_mp4_icon.svg"),
            cmd="Convert video to specific format",
            tip="Convert video to specific format",
        )

    def operate(self, editor: Editor):
        video_field_name = self.config[ConvertVideoFieldsKey.VIDEO_FIELD]
        video_field_value = editor.note[video_field_name]
        video_path = to_abs_path(video_field_value)

        manager = FFmpegManager(
            commands=[
                ConvertVideoFFmpegCommand(video_path, self.config)
            ],
            on_all_tasks_completed=lambda output_paths: self.post_process(editor, output_paths),
        )
        manager.start_ffmpeg_tasks()

    def post_process(self, editor, output_paths: List[str]):
        video_field_name = self.config[ConvertVideoFieldsKey.VIDEO_FIELD]
        editor.note[video_field_name] = to_sound_tag(output_paths.pop())

        self._redraw_note(editor)


class ExtractAudioButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={ExtractAudioFieldsKey.VIDEO_FIELD, ExtractAudioFieldsKey.AUDIO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "extract_audio_icon.svg"),
            cmd="Extract audio from video",
            tip="Extract audio from video and insert into field",
        )

    def operate(self, editor: Editor):
        video_field_name = self.config[ExtractAudioFieldsKey.VIDEO_FIELD]
        video_field_value = editor.note[video_field_name]
        video_path = to_abs_path(video_field_value)

        manager = FFmpegManager(
            commands=[
                ExtractAudioFFmpegCommand(video_path, self.config)
            ],
            on_all_tasks_completed=lambda output_paths: self.post_process(editor, output_paths),
        )
        manager.start_ffmpeg_tasks()

    def post_process(self, editor, output_paths: List[str]):
        audio_field_name = self.config[ExtractAudioFieldsKey.AUDIO_FIELD]
        editor.note[audio_field_name] = to_sound_tag(output_paths.pop())

        self._redraw_note(editor)


class EmbedMediaButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={
                EmbedMediaFieldsKey.VIDEO_FIELD,
                EmbedMediaFieldsKey.EMBEDDED_VIDEO_FIELD,
                EmbedMediaFieldsKey.AUDIO_FIELD,
                EmbedMediaFieldsKey.EMBEDDED_AUDIO_FIELD,
            },
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "embed_media_icon.svg"),
            cmd="Embed media",
            tip="Embed audio or video into field",
        )

    def operate(self, editor):
        current_field_name = self._get_selected_field_name(editor)
        current_field_value = editor.note[current_field_name]

        if current_field_name == self.config[EmbedMediaFieldsKey.VIDEO_FIELD]:
            video_path = to_abs_path(current_field_value)

            manager = FFmpegManager(
                commands=[
                    Mp4FFmpegCommand(video_path),
                    WebmFFmpegCommand(video_path),
                ],
                on_all_tasks_completed=lambda output_paths: self.post_video_process(editor, output_paths),
            )
            manager.start_ffmpeg_tasks()
        elif current_field_name == self.config[EmbedMediaFieldsKey.AUDIO_FIELD]:
            audio_path = to_abs_path(current_field_value)

            manager = FFmpegManager(
                commands=[
                    ExtractAudioFFmpegCommand(audio_path, self.config)
                ],
                on_all_tasks_completed=lambda output_paths: self.post_audio_process(editor, output_paths),
            )
            manager.start_ffmpeg_tasks()

    def post_video_process(self, editor, output_paths):
        embedder = HtmlMediaEmbedder(self.config)

        video_field_name = self.config[EmbedMediaFieldsKey.VIDEO_FIELD]
        editor.note[video_field_name] = "".join([to_sound_tag(output_path) for output_path in output_paths])

        embedded_video_field = self.config[EmbedMediaFieldsKey.EMBEDDED_VIDEO_FIELD]
        editor.note[embedded_video_field] = embedder.generate_video_tag(output_paths)

        self._redraw_note(editor)

    def post_audio_process(self, editor, output_paths):
        embedder = HtmlMediaEmbedder(self.config)

        output_path = output_paths.pop()

        audio_field_name = self.config[EmbedMediaFieldsKey.AUDIO_FIELD]
        editor.note[audio_field_name] = to_sound_tag(output_path)

        embedded_audio_field = self.config[EmbedMediaFieldsKey.EMBEDDED_AUDIO_FIELD]
        editor.note[embedded_audio_field] = embedder.generate_audio_tag(output_path)

        self._redraw_note(editor)


class SttButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={FieldKey.AUDIO_FIELD, FieldKey.STT_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "stt_icon.svg"),
            cmd="Speech to text",
            tip="Convert audio to text",
        )

    def operate(self, editor: Editor):
        audio_field_value = self._get_field_value(editor, FieldKey.AUDIO_FIELD)

        audio_path = to_abs_path(audio_field_value)

        transcription = speech_to_text(audio_path)

        stt_field = self._get_field_name(FieldKey.STT_FIELD)
        editor.note[stt_field] = transcription
