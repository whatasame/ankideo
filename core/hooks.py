from aqt import gui_hooks

from .gui import append_convert_button

def init_hooks() -> None:
    gui_hooks.editor_did_init_buttons.append(append_convert_button)
