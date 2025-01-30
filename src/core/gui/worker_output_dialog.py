from typing import Optional, Callable

from aqt import Qt, QDialog, QVBoxLayout, QTextEdit, QLabel, QWidget, QPushButton


class WorkerOutputDialog(QDialog):
    def __init__(self, parent: Optional[QWidget], num_tasks: int, on_cancel: Callable[[], None]) -> None:
        super().__init__(parent)
        self.num_tasks = num_tasks
        self.on_cancel = on_cancel

        # Remove window buttons
        self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.CustomizeWindowHint)

        layout = QVBoxLayout()

        self.output_texts = []
        for i in range(self.num_tasks):
            layout.addWidget(QLabel(f"Task {i + 1}:"))

            text_edit = QTextEdit()
            text_edit.setReadOnly(True)
            text_edit.setMinimumWidth(600)
            text_edit.setMaximumHeight(100)

            layout.addWidget(text_edit)

            self.output_texts.append(text_edit)

        self.interact_button = QPushButton("Cancel")
        self.interact_button.clicked.connect(self.on_cancel_clicked)
        layout.addWidget(self.interact_button)

        self.setLayout(layout)

    def append_output(self, index: int, text: str) -> None:
        self.output_texts[index].append(text)

    def on_cancel_clicked(self):
        self.on_cancel()
        self.close()
