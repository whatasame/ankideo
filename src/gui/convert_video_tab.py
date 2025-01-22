from aqt import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpinBox

from ..constants.convert_video_key import FieldsKey, FFmpegArgumentsKey
from ..core.config import Config


class ConvertVideoTab(QWidget):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

        layout = QHBoxLayout()
        self.setLayout(layout)

        field_layout = ConvertVideoFieldLayout(config)
        layout.addWidget(field_layout)

        ffmpeg_arguments_layout = ConvertVideoFFmpegArgumentsLayout(config)
        layout.addWidget(ffmpeg_arguments_layout)


class ConvertVideoFieldLayout(QWidget):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setup_ui()

    def setup_ui(self):
        for field_key in FieldsKey:
            label = QLabel(field_key.value)
            line_edit = QLineEdit(self.config.get(field_key))
            line_edit.textChanged.connect(lambda text, key=field_key: self.config.set(key, text))

            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)


class ConvertVideoFFmpegArgumentsLayout(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setup_ui()

    def setup_ui(self):
        # Width and Height
        size_layout = QHBoxLayout()
        self.width_input = QSpinBox()
        self.height_input = QSpinBox()
        self.width_input.setRange(1, 9999)
        self.height_input.setRange(1, 9999)
        self.width_input.setValue(self.config.get(FFmpegArgumentsKey.WIDTH))
        self.height_input.setValue(self.config.get(FFmpegArgumentsKey.HEIGHT))
        size_layout.addWidget(QLabel("Width:"))
        size_layout.addWidget(self.width_input)
        size_layout.addWidget(QLabel("Height:"))
        size_layout.addWidget(self.height_input)
        self.layout.addLayout(size_layout)

        # CRF
        crf_layout = QHBoxLayout()
        self.crf_input = QSpinBox()
        self.crf_input.setRange(0, 51)
        self.crf_input.setValue(self.config.get(FFmpegArgumentsKey.CRF))
        crf_layout.addWidget(QLabel("CRF:"))
        crf_layout.addWidget(self.crf_input)
        self.layout.addLayout(crf_layout)

        # Extension
        extension_layout = QHBoxLayout()
        self.extension_combo = QComboBox()
        self.extension_combo.addItems(["mp4", "webm"])
        self.extension_combo.setCurrentText(self.config.get(FFmpegArgumentsKey.EXTENSION))
        extension_layout.addWidget(QLabel("Extension:"))
        extension_layout.addWidget(self.extension_combo)
        self.layout.addLayout(extension_layout)

        # Audio Bitrate
        bitrate_layout = QHBoxLayout()
        self.bitrate_combo = QComboBox()
        self.bitrate_combo.addItems(["128k", "192k"])
        self.bitrate_combo.setCurrentText(self.config.get(FFmpegArgumentsKey.AUDIO_BITRATE))
        bitrate_layout.addWidget(QLabel("Audio Bitrate:"))
        bitrate_layout.addWidget(self.bitrate_combo)
        self.layout.addLayout(bitrate_layout)

        # Connect signals
        self.width_input.valueChanged.connect(
            lambda value, key=FFmpegArgumentsKey.WIDTH: self.config.set(key, value))
        self.height_input.valueChanged.connect(
            lambda value, key=FFmpegArgumentsKey.HEIGHT: self.config.set(key, value))
        self.crf_input.valueChanged.connect(
            lambda value, key=FFmpegArgumentsKey.CRF: self.config.set(key, value))
        self.extension_combo.currentTextChanged.connect(
            lambda text, key=FFmpegArgumentsKey.EXTENSION: self.config.set(key, text))
        self.bitrate_combo.currentTextChanged.connect(
            lambda text, key=FFmpegArgumentsKey.AUDIO_BITRATE: self.config.set(key, text))
