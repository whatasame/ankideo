import os
from pathlib import Path
from typing import List

from aqt.editor import Editor

from ..convert_command import ConvertVideoFFmpegCommand
from ..convert_constants import ConvertVideoFieldsKey
from ...core.ffmpeg.worker import FFmpegManager
from ...core.gui.editor_button import EditorButton
from ...core.models import SoundTag


class ConvertVideoFormatButton(EditorButton):
    def __init__(self) -> None:
        super().__init__(
            allowed_field_keys={ConvertVideoFieldsKey.VIDEO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../../assets", "convert_mp4_icon.svg"),
            cmd="Convert video to specific format",
            tip="Convert video to specific format",
        )

    def operate(self, editor: Editor) -> None:
        video_field_name = self.config[ConvertVideoFieldsKey.VIDEO_FIELD]
        video_field_value = editor.note[video_field_name]
        video_path = SoundTag(video_field_value).to_path()

        manager = FFmpegManager(
            commands=[
                ConvertVideoFFmpegCommand(video_path, self.config)
            ],
            on_all_tasks_completed=lambda output_paths: self.post_process(editor, output_paths),
            is_delete_input_files=True,
        )
        manager.start_ffmpeg_tasks()

    def post_process(self, editor: Editor, output_paths: List[Path]) -> None:
        video_field_name = self.config[ConvertVideoFieldsKey.VIDEO_FIELD]
        editor.note[video_field_name] = str(SoundTag(output_paths.pop()))

        self._redraw_note(editor)
