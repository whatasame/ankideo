from aqt.qt import QDialog, QVBoxLayout, QPushButton, QMessageBox, QTabWidget

from ...convert.gui.convert_preference import ConvertVideoPreferenceTab
from ...core.config import Config
from ...embed.gui.embed_preference import EmbedMediaPreferenceTab
from ...extract.gui.extract_preference import ExtractAudioPrefrenceTab
from ...stt.gui.stt_preference import SttPreferenceTab


class PreferenceDialog(QDialog):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        convert_video_tab = ConvertVideoPreferenceTab(config)
        self.tab_widget.addTab(convert_video_tab, "Convert Video")

        extract_audio_tab = ExtractAudioPrefrenceTab(config)
        self.tab_widget.addTab(extract_audio_tab, "Extract audio")

        embed_media_tab = EmbedMediaPreferenceTab(config)
        self.tab_widget.addTab(embed_media_tab, "Embed Media")

        stt_media_tab = SttPreferenceTab(config)
        self.tab_widget.addTab(stt_media_tab, "Speech to text")

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.on_save)
        main_layout.addWidget(save_button)

    def on_save(self):
        self.config.save()
        QMessageBox.information(self, "Success", "Settings saved")
        self.accept()
