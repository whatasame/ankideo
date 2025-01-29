import os

from aqt.editor import Editor

from ...core.gui.editor_button import EditorButton
from ...core.utils import to_abs_path


class SttButton(EditorButton):
    def __init__(self):
        super().__init__(
            allowed_field_keys={FieldKey.AUDIO_FIELD, FieldKey.STT_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../../assets", "stt_icon.svg"),
            cmd="Speech to text",
            tip="Convert audio to text",
        )

    def operate(self, editor: Editor):
        audio_field_value = self._get_field_value(editor, FieldKey.AUDIO_FIELD)

        audio_path = to_abs_path(audio_field_value)

        transcription = speech_to_text(audio_path)

        stt_field = self._get_field_name(FieldKey.STT_FIELD)
        editor.note[stt_field] = transcription
