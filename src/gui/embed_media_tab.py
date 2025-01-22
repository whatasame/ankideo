from aqt import *

from ..core.config import Config
from ..core.constants import EmbedMedia, AudioTagAttribute, VideoTagAttribute


class EmbedMediaTab(QWidget):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

        layout = QHBoxLayout()
        self.setLayout(layout)

        field_layout = EmbedMediaFieldLayout(config)
        layout.addWidget(field_layout)

        media_tag_layout = MediaTagAttributeLayout(config)
        layout.addWidget(media_tag_layout)


class EmbedMediaFieldLayout(QWidget):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setup_ui()

    def setup_ui(self):
        for field_key in EmbedMedia:
            label = QLabel(field_key.value)
            line_edit = QLineEdit(self.config.get(field_key))
            line_edit.textChanged.connect(lambda text, key=field_key: self.config.set(key, text))

            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)


class MediaTagAttributeLayout(QWidget):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setup_ui()

    def setup_ui(self):
        for attribute in [VideoTagAttribute, AudioTagAttribute]:
            group_box = QGroupBox(attribute.get_key_name())
            group_layout = QVBoxLayout()

            for attribute_key in attribute:
                checkbox = QCheckBox(attribute_key.value)
                checkbox.setChecked(self.config.get(attribute_key))
                checkbox.stateChanged.connect(lambda state, key=attribute_key: self.config.set(key, state))

                group_layout.addWidget(checkbox)

            group_box.setLayout(group_layout)
            self.layout.addWidget(group_box)
