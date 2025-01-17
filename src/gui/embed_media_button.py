import os
from typing import List

from aqt import mw
from aqt.editor import Editor

from ..constants import AUDIO_FIELD_KEY
from ..exception import AnkidiaError
from ..html_manager import build_audio_html
from ..utils import has_text, to_anki_media_path


def append_embed_media_button(exist_buttons: List[str], editor: Editor) -> None:
    embed_button = editor.addButton(
        icon=os.path.join(os.path.dirname(__file__), "../assets", "embed_media_icon.svg"),
        cmd="Embed media",
        func=lambda ed: on_click(ed),
        tip="Embed audio or video into field",
    )

    exist_buttons.append(embed_button)


def on_click(editor: Editor):
    config = mw.addonManager.getConfig(__name__)  # TODO: selected field
    audio_field = config[AUDIO_FIELD_KEY]

    if not audio_field in editor.note:
        raise AnkidiaError(f"Field '{audio_field}' doesn't exist in the note.")

    if not has_text(editor.note[audio_field]):
        raise AnkidiaError(f"'{audio_field}' field is empty.")

    audio_path = to_anki_media_path(editor.note[audio_field])
    editor.note[audio_field] = build_audio_html(audio_path)

    # redraw the editor. see more https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
    editor.set_note(editor.note)
