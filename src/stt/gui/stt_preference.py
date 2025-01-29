from aqt import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QComboBox

from ..stt_constants import SttFieldsKey, SttWhisperArgumentsKey


class SttPreferenceTab(QWidget):
    def __init__(self, config):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(SttFieldLayout(config))
        layout.addWidget(SttWhisperArgumentsLayout(config))


class SttFieldLayout(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setup_ui()

    def setup_ui(self):
        for field_key in SttFieldsKey:
            label = QLabel(field_key.value)
            line_edit = QLineEdit(self.config[field_key])
            line_edit.textChanged.connect(lambda text, key=field_key: self.config.set(key, text))

            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)


class SttWhisperArgumentsLayout(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setup_model_layout()

    def setup_model_layout(self):
        model_layout = QHBoxLayout()

        model_label = QLabel("Model:")
        model_layout.addWidget(model_label)

        model_combo = QComboBox()
        model_combo.addItems(["small"])
        model_combo.setCurrentText(self.config[SttWhisperArgumentsKey.MODEL])
        model_combo.currentTextChanged.connect(lambda text: self.config.set(SttWhisperArgumentsKey.MODEL, text))
        model_layout.addWidget(model_combo)

        self.layout.addLayout(model_layout)
