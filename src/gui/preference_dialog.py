from aqt.qt import QDialog, QVBoxLayout, QPushButton, QMessageBox, QTabWidget

from .embed_media_tab import EmbedMediaTab
from ..core.config import Config


class PreferenceDialog(QDialog):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        embed_media_tab = EmbedMediaTab(config)
        self.tab_widget.addTab(embed_media_tab, "Embed Media")

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.on_save)
        main_layout.addWidget(save_button)

    def on_save(self):
        self.config.save()
        QMessageBox.information(self, "Success", "Settings saved")
        self.accept()
