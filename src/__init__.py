from .hooks import init_hooks
from .setting_menu_item import build_setting_menu_item


def run():
    build_setting_menu_item()
    init_hooks()
