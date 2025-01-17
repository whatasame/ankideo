import os
from typing import List

from aqt import mw
from aqt.editor import Editor
from aqt.utils import tooltip

from text_utils import has_text, to_anki_media_path, to_sound_tag
from video_manager import extract_audio


def append_extract_button(exist_buttons: List[str], editor: Editor) -> None:
    extract_audio_button = editor.addButton(
        icon=os.path.join(os.path.dirname(__file__), "assets", "extract_audio_icon.svg"),
        cmd="Extract audio from video",
        func=lambda ed: on_click(ed),
        tip="Extract audio from video and insert into field",
    )

    exist_buttons.append(extract_audio_button)


def on_click(editor: Editor):
    config = mw.addonManager.getConfig(__name__)
    video_field = config["video_field"]
    audio_field = config["audio_field"]

    if not all(field in editor.note for field in (video_field, audio_field)):
        tooltip("Wrong field name. Please check the field name in the setting dialog.")
        return
    if not has_text(editor.note[video_field]):
        tooltip("The video field is empty.")
        return

    video_path = to_anki_media_path(editor.note[video_field])
    audio_path = extract_audio(video_path)
    editor.note[audio_field] = to_sound_tag(audio_path)

    # redraw the editor. see more https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
    editor.set_note(editor.note)
