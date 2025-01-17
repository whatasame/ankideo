from PyQt6.QtGui import QAction
from aqt import mw, qconnect

from setting_dialog import setting_dialog_open


def build_setting_menu_item():
    action = QAction("Ankidia options", mw)

    qconnect(action.triggered, setting_dialog_open)

    mw.form.menuTools.addAction(action)
