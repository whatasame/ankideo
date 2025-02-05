import os
from pathlib import Path
from typing import List

from aqt.editor import Editor

from ..embed_command import Mp4FFmpegCommand, WebmFFmpegCommand
from ..embed_constants import EmbedMediaFieldsKey
from ..html_tag_factory import HtmlTagFactory
from ...core.ffmpeg.worker import FFmpegManager
from ...core.gui.editor_button import EditorButton
from ...core.models import SoundTag


class EmbedMediaButton(EditorButton):
    def __init__(self) -> None:
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

    def operate(self, editor: Editor):
        current_field_name = self._get_selected_field_name(editor)

        if current_field_name == self.config[EmbedMediaFieldsKey.VIDEO_FIELD]:
            video_field_value = editor.note[current_field_name]
            video_path = SoundTag(video_field_value).to_path()

            manager = FFmpegManager(
                commands=[
                    Mp4FFmpegCommand(video_path),
                    WebmFFmpegCommand(video_path),
                ],
                on_all_tasks_completed=lambda output_paths: self.post_video_process(editor, output_paths),
                is_delete_input_files=True,
            )
            manager.start_ffmpeg_tasks()
        elif current_field_name == self.config[EmbedMediaFieldsKey.AUDIO_FIELD]:
            audio_field_value = editor.note[current_field_name]
            audio_path = SoundTag(audio_field_value).to_path()

            embedder = HtmlTagFactory(self.config)

            embedded_audio_field = self.config[EmbedMediaFieldsKey.EMBEDDED_AUDIO_FIELD]
            editor.note[embedded_audio_field] = embedder.generate_audio_tag(audio_path)

            self._redraw_note(editor)

    def post_video_process(self, editor: Editor, output_paths: List[Path]) -> None:
        embedder = HtmlTagFactory(self.config)

        video_field_name = self.config[EmbedMediaFieldsKey.VIDEO_FIELD]
        editor.note[video_field_name] = "".join(map(str, [SoundTag(output_path) for output_path in output_paths]))

        embedded_video_field = self.config[EmbedMediaFieldsKey.EMBEDDED_VIDEO_FIELD]
        editor.note[embedded_video_field] = embedder.generate_video_tag(output_paths)

        self._redraw_note(editor)
