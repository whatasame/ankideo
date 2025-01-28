import html
import os
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


def to_abs_path(text: str) -> str:
    sound_pattern = r"\[sound:(.*?)\]"

    matches = re.findall(sound_pattern, text)

    if not matches:
        raise AnkidiaError(f"No sound tag found. {text}")
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


def split_basename_and_extension(path: str) -> tuple[str, str]:
    basename = os.path.basename(path)
    extension = os.path.splitext(basename)[1][1:]  # remove the dot

    return basename, extension


def safe_remove_file(path):
    if os.path.exists(path):
        os.remove(path)
