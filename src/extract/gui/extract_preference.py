from aqt import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QHBoxLayout

from ..extract_constants import ExtractAudioFieldsKey, ExtractAudioFFmpegArgumentsKey
from ...core.config import Config


class ExtractAudioTab(QWidget):
    def __init__(self, config: Config):
        super().__init__()

        self.config = config

        layout = QVBoxLayout()
        self.setLayout(layout)

        field_layout = ExtractAudioFieldLayout(config)
        layout.addWidget(field_layout)

        ffmpeg_arguments_layout = ExtractAudioFFmpegArgumentsLayout(config)
        layout.addWidget(ffmpeg_arguments_layout)


class ExtractAudioFieldLayout(QWidget):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setup_ui()

    def setup_ui(self):
        for field_key in ExtractAudioFieldsKey:
            label = QLabel(field_key.value)
            line_edit = QLineEdit(self.config[field_key])
            line_edit.textChanged.connect(lambda text, key=field_key: self.config.set(key, text))

            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)


class ExtractAudioFFmpegArgumentsLayout(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setup_ui()

    def setup_ui(self):
        # Extension
        extension_layout = QHBoxLayout()
        self.extension_combo = QComboBox()
        self.extension_combo.addItems(["mp3"])
        self.extension_combo.setCurrentText(self.config[ExtractAudioFFmpegArgumentsKey.EXTENSION])
        extension_layout.addWidget(QLabel("Extension:"))
        extension_layout.addWidget(self.extension_combo)
        self.layout.addLayout(extension_layout)
        self.extension_combo.currentTextChanged.connect(
            lambda text: self.config.set(ExtractAudioFFmpegArgumentsKey.EXTENSION, text))

        # Bitrate
        bitrate_layout = QHBoxLayout()
        self.bitrate_combo = QComboBox()
        self.bitrate_combo.addItems(["192k"])
        self.bitrate_combo.setCurrentText(self.config[ExtractAudioFFmpegArgumentsKey.AUDIO_BITRATE])
        bitrate_layout.addWidget(QLabel("Audio bitrate:"))
        bitrate_layout.addWidget(self.bitrate_combo)
        self.layout.addLayout(bitrate_layout)
        self.bitrate_combo.currentTextChanged.connect(
            lambda text: self.config.set(ExtractAudioFFmpegArgumentsKey.AUDIO_BITRATE, text))
