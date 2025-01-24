from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPlainTextEdit, QPushButton


class FFmpegOutputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("FFmpeg log")
        self.setMinimumWidth(600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        self.cancel_button = QPushButton("Cancel")
        layout.addWidget(self.cancel_button)
