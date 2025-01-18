from typing import Any

from aqt import mw
from aqt.qt import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from ..core.constants import FieldKey


class PreferenceDialog(QDialog):
    def __init__(self, config: dict[str, Any]):
        super().__init__()

        self.config = config

        # Layout
        self.setLayout(QVBoxLayout())

        # Field ui
        self.line_edits = {}
        for field_key in [FieldKey.VIDEO_FIELD, FieldKey.AUDIO_FIELD, FieldKey.STT_FIELD]:
            self.add_field_ui(field_key)

        # Save button ui
        self.save_button = QPushButton("Save")

        self.save_button.clicked.connect(self.on_click_save)  # type: ignore # https://stackoverflow.com/a/78920397

        self.layout().addWidget(self.save_button)

    def add_field_ui(self, field_key: FieldKey):
        label = QLabel(field_key.value)
        self.layout().addWidget(label)

        line_edit = QLineEdit(self.config[field_key.value])
        self.layout().addWidget(line_edit)

        self.line_edits[field_key] = line_edit

    def on_click_save(self):
        for field_key, line_edit in self.line_edits.items():
            self.config[field_key.value] = line_edit.text()

        mw.addonManager.writeConfig(__name__, self.config)

        QMessageBox.information(self, "Success", "Setting saved")

        self.accept()
