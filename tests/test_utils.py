from unittest import TestCase
from unittest.mock import patch

from core.utils import *


class TestHasText(TestCase):
    def test_empty_string(self):
        self.assertFalse(has_text(""))

    def test_none_input(self):
        self.assertFalse(has_text(None))

    def test_whitespace_only(self):
        self.assertFalse(has_text("   "))

    def test_plain_text(self):
        self.assertTrue(has_text("Hello, World!"))

    def test_text_with_whitespace(self):
        self.assertTrue(has_text("  Hello, World!  "))


class TestHtmlStrip(TestCase):
    def test_nbsp(self):
        self.assertEqual("", html_strip("&nbsp;"))

    def test_html_entities(self):
        self.assertEqual("<div>Hello</div>", html_strip("&lt;div&gt;Hello&lt;/div&gt;"))

    def test_leading_trailing_whitespace(self):
        self.assertEqual("Hello World", html_strip("  Hello World  "))

    def test_combined_html_and_whitespace(self):
        self.assertEqual("<div>Hello</div>", html_strip("  &lt;div&gt;Hello&lt;/div&gt;  "))


class TestToAnkiMediaPath(TestCase):
    @patch('text_utils.mw')
    def test_only_one_sound_tag(self, mock_mw):
        mock_mw.col.media.dir.return_value = '/path/to/media'

        text = "[sound:test.mp3]"

        result = to_abs_path(text)

        self.assertEqual("/path/to/media/test.mp3", result)

    @patch('text_utils.mw')
    def test_mixed_up_sound_tag(self, mock_mw):
        mock_mw.col.media.dir.return_value = '/path/to/media'

        text = "Hello, [sound:test.mp3] World!"

        result = to_abs_path(text)

        self.assertEqual("/path/to/media/test.mp3", result)

    def test_more_than_one_sound_tag(self):
        text = "[sound:test.mp3][sound:test2.mp3]"

        with self.assertRaises(AnkidiaError) as context:
            to_abs_path(text)

        self.assertEqual("More than one sound tag found.", str(context.exception))

    def test_no_sound_tag(self):
        text = "test.mp3"

        with self.assertRaises(AnkidiaError) as context:
            to_abs_path(text)

        self.assertEqual("No sound tag found.", str(context.exception))


class TestToSoundTag(TestCase):
    @patch('os.path.isfile', return_value=True)
    def test_valid_path(self, mock_isfile):
        path = "/path/to/media/test.mp3"

        result = to_sound_tag(path)

        self.assertEqual("[sound:test.mp3]", result)


class TestCheckFileExist(TestCase):
    def test_empty_path(self):
        path = ""

        with self.assertRaises(AnkidiaError) as context:
            check_file_exist(path)

        self.assertEqual("Empty path.", str(context.exception))

    def test_file_not_found(self):
        path = "/hello/world/poop/nonexistent.mp3"

        with self.assertRaises(AnkidiaError) as context:
            check_file_exist(path)

        self.assertEqual(f"File not found: {path}", str(context.exception))
