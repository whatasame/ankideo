import os

from aqt.editor import Editor

from ..stt_constants import SttFieldsKey
from ..whisper_service import WhisperService
from ...core.gui.editor_button import EditorButton
from ...core.utils import to_abs_path


class SttButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={SttFieldsKey.AUDIO_FIELD, SttFieldsKey.STT_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../../assets", "stt_icon.svg"),
            cmd="Speech to text",
            tip="Convert audio to text",
        )

    def operate(self, editor: Editor):
        audio_field_name = self.config[SttFieldsKey.AUDIO_FIELD]
        audio_field_value = editor.note[audio_field_name]
        audio_path = to_abs_path(audio_field_value)

        whisper_service = WhisperService(self.config)
        transcription = whisper_service.transcribe(audio_path)

        stt_field_name = self.config[SttFieldsKey.STT_FIELD]
        editor.note[stt_field_name] = transcription

        self._redraw_note(editor)
        
