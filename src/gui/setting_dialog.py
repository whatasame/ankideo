from typing import Any

from aqt import mw
from aqt.qt import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class SettingDialog(QDialog):
    def __init__(self, config: dict[str, Any]):
        super().__init__()

        self.config = config

        # Layout
        self.setLayout(QVBoxLayout())

        # Video field ui
        self.video_label = QLabel("Video field name")
        self.video_line_edit = QLineEdit(config["video_field"])

        self.layout().addWidget(self.video_label)
        self.layout().addWidget(self.video_line_edit)

        # Audio field ui
        self.audio_label = QLabel("Audio field name")
        self.audio_line_edit = QLineEdit(config["audio_field"])

        self.layout().addWidget(self.audio_label)
        self.layout().addWidget(self.audio_line_edit)

        # STT field ui
        self.stt_label = QLabel("STT field name")
        self.stt_line_edit = QLineEdit(config["stt_field"])

        self.layout().addWidget(self.stt_label)
        self.layout().addWidget(self.stt_line_edit)

        # Save button ui
        self.save_button = QPushButton("Save")

        self.save_button.clicked.connect(self.on_click_save)  # type: ignore # https://stackoverflow.com/a/78920397

        self.layout().addWidget(self.save_button)

    def on_click_save(self):
        video_field = self.video_line_edit.text()
        audio_field = self.audio_line_edit.text()
        stt_field = self.stt_line_edit.text()

        self.config["video_field"] = video_field
        self.config["audio_field"] = audio_field
        self.config["stt_field"] = stt_field
        mw.addonManager.writeConfig(__name__, self.config)

        QMessageBox.information(self, "Success", "Setting saved")

        self.accept()


def setting_dialog_open():
    config = mw.addonManager.getConfig(__name__)

    dialog = SettingDialog(config)
    dialog.show()
    dialog.exec()
