from typing import List, Any

from aqt import mw
from aqt.editor import Editor
from aqt.qt import QAction, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from aqt.utils import tooltip, qconnect


def append_convert_button(exist_buttons: List[str], editor: Editor) -> None:
    new_btn = editor.addButton(
        icon=None,
        cmd="Convert mp4 to mp3",
        func=lambda ed: tooltip("Converted"),
        tip="Convert mp4 file in input field to mp3 and insert into output field",
        label="Convert",
    )

    exist_buttons.append(new_btn)


def setting_menu_item():
    action = QAction("mp4 to mp3 options", mw)

    qconnect(action.triggered, setting_dialog_open)

    mw.form.menuTools.addAction(action)


class SettingDialog(QDialog):
    def __init__(self, config: dict[str, Any]):
        super().__init__()

        self.config = config

        # Layout
        self.setLayout(QVBoxLayout())

        # Source field ui
        self.source_label = QLabel("Source field name")
        self.source_line_edit = QLineEdit(config["source_field"])

        self.layout().addWidget(self.source_label)
        self.layout().addWidget(self.source_line_edit)

        # Target field ui
        self.target_label = QLabel("target field name")
        self.target_line_edit = QLineEdit(config["target_field"])

        self.layout().addWidget(self.target_label)
        self.layout().addWidget(self.target_line_edit)

        # Save button ui
        self.save_button = QPushButton("Save")

        self.save_button.clicked.connect(self.on_click_save)  # type: ignore # https://stackoverflow.com/a/78920397

        self.layout().addWidget(self.save_button)

    def on_click_save(self):
        source_field = self.source_line_edit.text()
        target_field = self.target_line_edit.text()

        self.config["source_field"] = source_field
        self.config["target_field"] = target_field
        mw.addonManager.writeConfig(__name__, self.config)

        QMessageBox.information(self, "Success", "Setting saved")

        self.accept()


def setting_dialog_open():
    config = mw.addonManager.getConfig(__name__)

    dialog = SettingDialog(config)
    dialog.show()
    dialog.exec()
