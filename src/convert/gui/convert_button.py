import os
from typing import List

from aqt.editor import Editor

from ..convert_command import ConvertVideoFFmpegCommand
from ..convert_constants import ConvertVideoFieldsKey
from ...core.ffmpeg.worker import FFmpegManager
from ...core.gui.editor_button import EditorButton
from ...core.utils import to_abs_path, to_sound_tag


class ConvertVideoFormatButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={ConvertVideoFieldsKey.VIDEO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../../assets", "convert_mp4_icon.svg"),
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
