import html
import os.path
import re

from aqt import mw

from .exception import AnkidiaError


def has_text(text: str) -> bool:
    if not text:
        return False

    return bool(html_strip(text))


def html_strip(text: str) -> str:
    return html.unescape(text).strip()


def to_anki_media_path(text: str) -> str:
    sound_pattern = r"\[sound:(.*?)\]"

    matches = re.findall(sound_pattern, text)

    if not matches:
        raise AnkidiaError("No sound tag found.")
    if len(matches) > 1:
        raise AnkidiaError("More than one sound tag found.")

    basename = matches.pop()

    return os.path.join(mw.col.media.dir(), basename)


def to_sound_tag(path: str) -> str:
    check_file_exist(path)

    return f"[sound:{os.path.basename(path)}]"


def check_file_exist(path):
    if not has_text(path):
        raise AnkidiaError("Empty path.")

    if not os.path.isfile(path):
        raise AnkidiaError(f"File not found: {path}")
