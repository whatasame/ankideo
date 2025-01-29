import os
from typing import List

from aqt.editor import Editor

from ..extract_command import ExtractAudioFFmpegCommand
from ..extract_constants import ExtractAudioFieldsKey
from ...core.ffmpeg.worker import FFmpegManager
from ...core.gui.editor_button import EditorButton
from ...core.models import SoundTag


class ExtractAudioButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={ExtractAudioFieldsKey.VIDEO_FIELD, ExtractAudioFieldsKey.AUDIO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../../assets", "extract_audio_icon.svg"),
            cmd="Extract audio from video",
            tip="Extract audio from video and insert into field",
        )

    def operate(self, editor: Editor):
        video_field_name = self.config[ExtractAudioFieldsKey.VIDEO_FIELD]
        video_field_value = editor.note[video_field_name]
        video_path = SoundTag(video_field_value).to_path()

        manager = FFmpegManager(
            commands=[
                ExtractAudioFFmpegCommand(video_path, self.config)
            ],
            on_all_tasks_completed=lambda output_paths: self.post_process(editor, output_paths),
        )
        manager.start_ffmpeg_tasks()

    def post_process(self, editor: Editor, output_paths: List[str]) -> None:
        audio_field_name = self.config[ExtractAudioFieldsKey.AUDIO_FIELD]
        editor.note[audio_field_name] = str(SoundTag(output_paths.pop()))

        self._redraw_note(editor)
