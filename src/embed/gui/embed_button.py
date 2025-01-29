import os

from ..embed_command import Mp4FFmpegCommand, WebmFFmpegCommand
from ..embed_constants import EmbedMediaFieldsKey
from ..html_tag_factory import HtmlTagFactory
from ...core.ffmpeg.worker import FFmpegManager
from ...core.gui.editor_button import EditorButton
from ...core.utils import to_abs_path, to_sound_tag
from ...extract.extract_command import ExtractAudioFFmpegCommand


class EmbedMediaButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={
                EmbedMediaFieldsKey.VIDEO_FIELD,
                EmbedMediaFieldsKey.EMBEDDED_VIDEO_FIELD,
                EmbedMediaFieldsKey.AUDIO_FIELD,
                EmbedMediaFieldsKey.EMBEDDED_AUDIO_FIELD,
            },
            icon_path=os.path.join(os.path.dirname(__file__), "../../assets", "embed_media_icon.svg"),
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
        embedder = HtmlTagFactory(self.config)

        video_field_name = self.config[EmbedMediaFieldsKey.VIDEO_FIELD]
        editor.note[video_field_name] = "".join([to_sound_tag(output_path) for output_path in output_paths])

        embedded_video_field = self.config[EmbedMediaFieldsKey.EMBEDDED_VIDEO_FIELD]
        editor.note[embedded_video_field] = embedder.generate_video_tag(output_paths)

        self._redraw_note(editor)

    def post_audio_process(self, editor, output_paths):
        embedder = HtmlTagFactory(self.config)

        output_path = output_paths.pop()

        audio_field_name = self.config[EmbedMediaFieldsKey.AUDIO_FIELD]
        editor.note[audio_field_name] = to_sound_tag(output_path)

        embedded_audio_field = self.config[EmbedMediaFieldsKey.EMBEDDED_AUDIO_FIELD]
        editor.note[embedded_audio_field] = embedder.generate_audio_tag(output_path)

        self._redraw_note(editor)
