from typing import Any

from aqt import mw
from aqt.qt import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


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
