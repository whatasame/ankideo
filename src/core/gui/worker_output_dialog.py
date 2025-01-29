from aqt import QDialog, QVBoxLayout, QTextEdit, QLabel


class WorkerOutputDialog(QDialog):
    def __init__(self, num_tasks, parent=None):
        super().__init__(parent)
        self.num_tasks = num_tasks
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.output_texts = []
        for i in range(self.num_tasks):
            text_edit = QTextEdit()
            text_edit.setReadOnly(True)
            text_edit.setMinimumWidth(600)
            text_edit.setMaximumHeight(100)
            layout.addWidget(QLabel(f"Task {i + 1}:"))
            layout.addWidget(text_edit)
            self.output_texts.append(text_edit)
        self.setLayout(layout)

    def append_output(self, text, index):
        self.output_texts[index].append(text)

    def task_completed(self, index):
        self.output_texts[index].append("\n--- Task Completed ---")
