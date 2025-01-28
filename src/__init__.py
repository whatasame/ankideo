import sys

from PyQt6.QtGui import QAction
from aqt import gui_hooks, mw, qconnect
from aqt.utils import tooltip

from .core.config import Config
from .core.exception import AnkidiaError
from .gui.editor_button import ConvertVideoFormatButton, EditorButton, ExtractAudioButton, EmbedMediaButton
from .gui.preference_dialog import PreferenceDialog


def run():
    init_exception_handler()
    init_preference_dialog()
    init_editor_button()


def init_exception_handler():
    def ankidia_exception_handler(exctype, value, traceback):
        if isinstance(value, AnkidiaError):
            tooltip(value.message)
        else:
            sys.__excepthook__(exctype, value, traceback)

    sys.excepthook = ankidia_exception_handler


def init_preference_dialog():
    def on_click():
        dialog = PreferenceDialog(Config())
        dialog.show()
        dialog.exec()

    action = QAction("Ankidia preference", mw)

    qconnect(action.triggered, on_click)

    mw.form.menuTools.addAction(action)


def init_editor_button():
    new_buttons = [
        ConvertVideoFormatButton(),
        ExtractAudioButton(),
        # SttButton(),
        EmbedMediaButton(),
    ]

    def build_button_handler(btn: EditorButton):
        return lambda exist_buttons, editor: exist_buttons.append(
            editor.addButton(
                icon=btn.icon_path,
                cmd=btn.cmd,
                func=lambda ed: btn.on_click(ed),
                tip=btn.tip,
            )
        )

    for button in new_buttons:
        gui_hooks.editor_did_init_buttons.append(build_button_handler(button))
