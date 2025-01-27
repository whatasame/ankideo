from aqt.qt import QDialog, QVBoxLayout, QPushButton, QMessageBox, QTabWidget

from .convert_video_tab import ConvertVideoTab
from .embed_media_tab import EmbedMediaTab
from .extract_audio_tab import ExtractAudioTab
from ..core.config import Config


class PreferenceDialog(QDialog):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        convert_video_tab = ConvertVideoTab(config)
        self.tab_widget.addTab(convert_video_tab, "Convert Video")

        extract_audio_tab = ExtractAudioTab(config)
        self.tab_widget.addTab(extract_audio_tab, "Extract audio")

        embed_media_tab = EmbedMediaTab(config)
        self.tab_widget.addTab(embed_media_tab, "Embed Media")

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.on_save)
        main_layout.addWidget(save_button)

    def on_save(self):
        self.config.save()
        QMessageBox.information(self, "Success", "Settings saved")
        self.accept()
