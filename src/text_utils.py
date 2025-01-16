import html
import os.path
import re

from aqt import mw


def has_text(text: str) -> bool:
    if not text:
        return False

    return bool(html_strip(text))


def html_strip(text: str) -> str:
    return html.unescape(text).strip()


def to_anki_media_path(tag: str) -> str:
    sound_pattern = r"\[sound:(.*?)\]"

    basename = re.search(sound_pattern, tag).group(1)

    return os.path.join(mw.col.media.dir(), basename)


def to_sound_tag(path: str) -> str:
    return f"[sound:{os.path.basename(path)}]"
