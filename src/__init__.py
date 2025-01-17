from aqt import gui_hooks

from .exception import init_exception_handler
from .gui.convert_button import append_convert_button
from .gui.extract_button import append_extract_button
from .gui.setting_menu_item import build_setting_menu_item


def run():
    init_exception_handler()

    build_setting_menu_item()

    gui_hooks.editor_did_init_buttons.append(append_extract_button)
    gui_hooks.editor_did_init_buttons.append(append_convert_button)
