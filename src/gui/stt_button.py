import os
from typing import List

from aqt import mw
from aqt.editor import Editor

from ..audio_manager import speech_to_text
from ..constants import AUDIO_FIELD_KEY, STT_FIELD_KEY
from ..exception import AnkidiaError
from ..utils import has_text, to_anki_media_path


def append_stt_button(exist_buttons: List[str], editor: Editor) -> None:
    stt_button = editor.addButton(
        icon=os.path.join(os.path.dirname(__file__), "../assets", "stt_icon.svg"),
        cmd="Speech to text",
        func=lambda ed: on_click(ed),
        tip="Speech to text",
    )

    exist_buttons.append(stt_button)


def on_click(editor: Editor):
    config = mw.addonManager.getConfig(__name__)
    audio_field = config[AUDIO_FIELD_KEY]
    stt_field = config[STT_FIELD_KEY]

    for field in [audio_field, stt_field]:
        if not field in editor.note:
            raise AnkidiaError(f"Field '{field}' doesn't exist in the note.")

    if not has_text(editor.note[audio_field]):
        raise AnkidiaError(f"'{audio_field}' field is empty.")

    audio_path = to_anki_media_path(editor.note[audio_field])
    text = speech_to_text(audio_path)
    editor.note[stt_field] = text

    # redraw the editor. see more https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
    editor.set_note(editor.note)
