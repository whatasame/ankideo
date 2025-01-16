import os
from typing import List

from aqt import mw
from aqt.editor import Editor
from aqt.utils import tooltip

from .converter import extract_audio
from .text_utils import has_text, to_anki_media_path, to_sound_tag


def append_convert_button(exist_buttons: List[str], editor: Editor) -> None:
    new_btn = editor.addButton(
        icon=os.path.join(os.path.dirname(__file__), "assets", "icon.svg"),
        cmd="Convert mp4 to mp3",
        func=lambda ed: on_click(ed),
        tip="Convert mp4 file in input field to mp3 and insert into output field",
    )

    exist_buttons.append(new_btn)


def on_click(editor: Editor):
    config = mw.addonManager.getConfig(__name__)
    source_field = config["source_field"]
    target_field = config["target_field"]

    if not all(field in editor.note for field in (source_field, target_field)):
        tooltip("Wrong field name. Please check the field name in the setting dialog.")
        return
    if not has_text(editor.note[source_field]):
        tooltip("The source field is empty.")
        return

    video_path = to_anki_media_path(editor.note[source_field])
    audio_path = extract_audio(video_path)
    editor.note[target_field] = to_sound_tag(audio_path)

    # redraw the editor. see more https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
    editor.set_note(editor.note)
