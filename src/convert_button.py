import os
from typing import List

from aqt import mw
from aqt.editor import Editor
from aqt.utils import tooltip

from .text_utils import has_text, to_anki_media_path, to_sound_tag
from .video_manager import convert_to_mp4


def append_convert_button(exist_buttons: List[str], editor: Editor) -> None:
    convert_mp4_button = editor.addButton(
        icon=os.path.join(os.path.dirname(__file__), "assets", "convert_mp4_icon.svg"),
        cmd="Convert video to mp4",
        func=lambda ed: on_click(ed),
        tip="Convert video to mp4",
    )

    exist_buttons.append(convert_mp4_button)


def on_click(editor: Editor):
    config = mw.addonManager.getConfig(__name__)
    video_field = config["video_field"]

    if not video_field in editor.note:
        tooltip("Wrong field name. Please check the field name in the setting dialog.")
        return

    if not has_text(editor.note[video_field]):
        tooltip("The video field is empty.")
        return

    video_path = to_anki_media_path(editor.note[video_field])
    mp4_path = convert_to_mp4(video_path)
    editor.note[video_field] = to_sound_tag(mp4_path)

    # redraw the editor. see more https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
    editor.set_note(editor.note)
