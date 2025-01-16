from aqt import gui_hooks

from .convert_button import append_convert_button
from .extract_button import append_extract_button
from .setting_menu_item import build_setting_menu_item


def run():
    build_setting_menu_item()

    gui_hooks.editor_did_init_buttons.append(append_extract_button)
    gui_hooks.editor_did_init_buttons.append(append_convert_button)
