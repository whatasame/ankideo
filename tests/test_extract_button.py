from unittest import TestCase
from unittest.mock import Mock, patch

from gui.extract_button import on_click, AnkidiaError


class TestOnClick(TestCase):

    @patch('extract_button.mw')
    def test_missing_video_field(self, mock_mw):
        mock_mw.addonManager.getConfig.return_value = {"video_field": "video", "audio_field": "audio"}
        editor = Mock()
        editor.note = {"audio": "some_audio_data"}

        with self.assertRaises(AnkidiaError) as context:
            on_click(editor)

        self.assertEqual("Field 'video' doesn't exist in the note.", str(context.exception))

    @patch('extract_button.mw')
    def test_missing_audio_field(self, mock_mw):
        mock_mw.addonManager.getConfig.return_value = {"video_field": "video", "audio_field": "audio"}
        editor = Mock()
        editor.note = {"video": "some_video_data"}

        with self.assertRaises(AnkidiaError) as context:
            on_click(editor)

        self.assertEqual("Field 'audio' doesn't exist in the note.", str(context.exception))

    @patch('extract_button.mw')
    def test_missing_both_fields(self, mock_mw):
        mock_mw.addonManager.getConfig.return_value = {"video_field": "video", "audio_field": "audio"}
        editor = Mock()
        editor.note = {}

        with self.assertRaises(AnkidiaError) as context:
            on_click(editor)

        self.assertEqual("Field 'video' doesn't exist in the note.", str(context.exception))

    @patch('extract_button.mw')
    def test_empty_video_field(self, mock_mw):
        editor = Mock()
        editor.note = {"video": "", "audio": ""}
        mock_mw.addonManager.getConfig.return_value = {"video_field": "video", "audio_field": "audio"}

        with self.assertRaises(AnkidiaError) as context:
            on_click(editor)

        self.assertEqual("'video' field is empty.", str(context.exception))
