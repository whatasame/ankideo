import unittest
from unittest.mock import patch

from service.html_service import build_audio_html

from core.exception import AnkidiaError


class TestBuildAudioHtml(unittest.TestCase):

    @patch('html_manager.check_file_exist')
    def test_valid_audio_file(self, mock_check_file_exist):
        mock_check_file_exist.return_value = None

        audio_path = '/path/to/audio/test.mp3'
        expected_html = """
<audio controls>
    <source src="/path/to/audio/test.mp3" type="audio/mp3">
    Your browser does not support the audio element.
</audio>
            """.strip()

        result = build_audio_html(audio_path)

        self.assertEqual(result, expected_html)

    @patch('html_manager.check_file_exist')
    def test_invalid_audio_file(self, mock_check_file_exist):
        mock_check_file_exist.side_effect = AnkidiaError("File not found")  # 예외를 발생시킴

        audio_path = '/path/to/audio/non_existent.mp3'

        with self.assertRaises(AnkidiaError) as context:
            build_audio_html(audio_path)

        self.assertEqual(str(context.exception), "File not found")
