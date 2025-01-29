from aqt import *

from ..constants.embed_media_key import EmbedMediaFieldsKey, EmbedVideoTagAttributesKey, EmbedAudioTagAttributesKey
from ..core.config import Config


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
        for field_key in EmbedMediaFieldsKey:
            label = QLabel(field_key.value)
            line_edit = QLineEdit(self.config[field_key])
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
        self.setup_video_attributes()
        self.setup_audio_attributes()

    def setup_video_attributes(self):
        group_box = QGroupBox(EmbedVideoTagAttributesKey.get_key_name())
        group_layout = QVBoxLayout()
        self._setup_attribute_group(EmbedVideoTagAttributesKey, group_layout)
        group_box.setLayout(group_layout)
        self.layout.addWidget(group_box)

    def setup_audio_attributes(self):
        group_box = QGroupBox(EmbedAudioTagAttributesKey.get_key_name())
        group_layout = QVBoxLayout()
        self._setup_attribute_group(EmbedAudioTagAttributesKey, group_layout)
        group_box.setLayout(group_layout)
        self.layout.addWidget(group_box)

    def _setup_attribute_group(self, attribute_class, group_layout):
        for attribute_key in attribute_class:
            if attribute_key == attribute_class.STYLE:
                self._add_line_edit(attribute_key, group_layout)
            elif attribute_key == attribute_class.SOURCE_FORMATS:
                self._add_format_selection(attribute_key, group_layout)
            else:
                self._add_checkbox(attribute_key, group_layout)

    def _add_line_edit(self, attribute_key, group_layout):
        label = QLabel(attribute_key.value)
        line_edit = QLineEdit(self.config[attribute_key])
        line_edit.textChanged.connect(lambda text, key=attribute_key: self.config.set(key, text))
        group_layout.addWidget(label)
        group_layout.addWidget(line_edit)

    def _add_checkbox(self, attribute_key, group_layout):
        checkbox = QCheckBox(attribute_key.value)
        checkbox.setChecked(self.config[attribute_key])
        checkbox.stateChanged.connect(
            lambda state, key=attribute_key: self.config.set(key, state == Qt.CheckState.Checked))
        group_layout.addWidget(checkbox)

    def _add_format_selection(self, attribute_key, group_layout):
        label = QLabel(attribute_key.value)
        format_list = QListWidget()
        formats = self.config[attribute_key]
        for format in formats:
            item = QListWidgetItem(format)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(
                Qt.CheckState.Checked if format in self.config[attribute_key] else Qt.CheckState.Unchecked)
            format_list.addItem(item)

        format_list.itemChanged.connect(lambda item: self._update_formats(attribute_key, format_list))

        group_layout.addWidget(label)
        group_layout.addWidget(format_list)

    def _update_formats(self, attribute_key, format_list):
        selected_formats = [format_list.item(i).text() for i in range(format_list.count())
                            if format_list.item(i).checkState() == Qt.CheckState.Checked]
        self.config.set(attribute_key, selected_formats)
