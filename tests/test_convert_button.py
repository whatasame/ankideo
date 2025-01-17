from unittest import TestCase
from unittest.mock import Mock, patch

from gui.convert_button import on_click, AnkidiaError


class TestOnClick(TestCase):

    @patch('convert_button.mw')
    def test_wrong_field_name(self, mock_mw):
        editor = Mock()
        editor.note = {}
        mock_mw.addonManager.getConfig.return_value = {"video_field": "wrong_field"}

        with self.assertRaises(AnkidiaError) as context:
            on_click(editor)

        self.assertEqual("Field 'wrong_field' doesn't exist in the note.", str(context.exception))

    @patch('convert_button.mw')
    def test_empty_video_field(self, mock_mw):
        editor = Mock()
        editor.note = {"Video": ""}
        mock_mw.addonManager.getConfig.return_value = {"video_field": "Video"}

        with self.assertRaises(AnkidiaError) as context:
            on_click(editor)

        self.assertEqual("'Video' field is empty.", str(context.exception))
