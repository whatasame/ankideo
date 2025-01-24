import os
from abc import abstractmethod
from typing import Set

from aqt.editor import Editor

from ..constants.convert_video_key import ConvertVideoFieldsKey
from ..constants.extract_audio_key import ExtractAudioFieldsKey
from ..constants.json_key import JsonKey
from ..core.config import Config
from ..core.exception import AnkidiaError
from ..core.old_constants import FieldKey
from ..core.old_constants import SupportedVideoExtension
from ..core.utils import to_abs_path, to_sound_tag
from ..ffmpeg.commands import ConvertFFmpegCommand, ExtractAudioFFmpegCommand
from ..ffmpeg.worker import FFmpegWorker
from ..service.ffmpeg_service import convert_compatibles
from ..service.html_service import build_audio_html, build_video_html
from ..service.whisper_service import speech_to_text


class EditorButton:
    def __init__(self, allowed_field_keys: Set[JsonKey], icon_path: str, cmd: str, tip: str):
        self.field_keys = allowed_field_keys
        self.icon_path = icon_path
        self.cmd = cmd
        self.tip = tip

    def on_click(self, editor: Editor):
        self._validate_field(editor)

        self.operate(editor)

    def _validate_field(self, editor):
        """
        Validate if the fields are existed in the note
        """
        config = Config()

        for field_key in self.field_keys:
            field_name = config[field_key]

            if not field_name in editor.note:
                raise AnkidiaError(f"Field '{field_name}' doesn't exist in the note.")

    @abstractmethod
    def operate(self, editor):
        pass

    def _redraw_editor(self, editor):
        # Redraw editor see more https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
        editor.set_note(editor.note)

    def _get_focus_field_name(self, editor: Editor):
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
            cmd="Convert video to mp4",
            tip="Convert video to mp4",
        )

    def operate(self, editor: Editor):
        config = Config()
        video_field_name = config[ConvertVideoFieldsKey.VIDEO_FIELD]
        video_field_value = editor.note[video_field_name]
        video_path = to_abs_path(video_field_value)

        ffmpeg_command = ConvertFFmpegCommand(video_path, config)
        FFmpegWorker(ffmpeg_command, lambda output_path: self.post_process(editor, output_path)).run()

    def post_process(self, editor, output_path):
        config = Config()
        video_field_name = config[ConvertVideoFieldsKey.VIDEO_FIELD]
        editor.note[video_field_name] = to_sound_tag(output_path)

        self._redraw_editor(editor)


class ExtractAudioButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={ExtractAudioFieldsKey.VIDEO_FIELD, ExtractAudioFieldsKey.AUDIO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "extract_audio_icon.svg"),
            cmd="Extract audio from video",
            tip="Extract audio from video and insert into field",
        )

    def operate(self, editor: Editor):
        config = Config()

        video_field_name = config[ExtractAudioFieldsKey.VIDEO_FIELD]
        video_field_value = editor.note[video_field_name]
        video_path = to_abs_path(video_field_value)

        ffmpeg_command = ExtractAudioFFmpegCommand(video_path, config)
        FFmpegWorker(ffmpeg_command, lambda output_path: self.post_process(editor, output_path)).run()

    def post_process(self, editor, output_path):
        config = Config()

        audio_field_name = config[ExtractAudioFieldsKey.AUDIO_FIELD]
        editor.note[audio_field_name] = to_sound_tag(output_path)

        self._redraw_editor(editor)


class EmbedMediaButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={
                FieldKey.VIDEO_FIELD,
                FieldKey.EMBEDDED_VIDEO_FIELD,
                FieldKey.AUDIO_FIELD,
                FieldKey.EMBEDDED_AUDIO_FIELD,
            },
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "embed_media_icon.svg"),
            cmd="Embed media",
            tip="Embed audio or video into field",
        )

    def operate(self, editor: Editor):
        current_field_name = self._get_focus_field_name(editor)
        if current_field_name == self._get_field_name(FieldKey.VIDEO_FIELD):
            self._embed_video(editor, current_field_name)
        elif current_field_name == self._get_field_name(FieldKey.AUDIO_FIELD):
            self._embed_audio(editor, current_field_name)
        else:
            raise AnkidiaError("Not a audio or video field")

    def _embed_video(self, editor: Editor, video_field_name: str):
        video_field_value = self._get_field_value(editor, FieldKey.VIDEO_FIELD)
        video_path = to_abs_path(video_field_value)
        video_paths = convert_compatibles(video_path, SupportedVideoExtension.MAC, SupportedVideoExtension.IOS)
        editor.note[video_field_name] = "".join([to_sound_tag(video_path) for video_path in video_paths])

        embedded_video_field_name = self._get_field_name(FieldKey.EMBEDDED_VIDEO_FIELD)
        editor.note[embedded_video_field_name] = build_video_html(video_paths)

    def _embed_audio(self, editor: Editor, audio_field_name: str):
        audio_field_value = self._get_field_value(editor, FieldKey.AUDIO_FIELD)
        audio_path = to_abs_path(audio_field_value)
        embedded_audio_field_name = self._get_field_name(FieldKey.EMBEDDED_AUDIO_FIELD)
        editor.note[embedded_audio_field_name] = build_audio_html(audio_path)


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
