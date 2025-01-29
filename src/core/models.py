import re
from pathlib import Path
from typing import Final, Union

from aqt import mw


class SoundTag:
    SOUND_PATTERN: Final = re.compile(r'\[sound:(.*?)\]')

    def __init__(self, source: Union[str, Path]) -> None:
        if isinstance(source, Path):
            self.basename = source.name
        elif isinstance(source, str):
            matches = re.findall(self.SOUND_PATTERN, source)

            if not matches:
                raise ValueError(f"No sound tag found. {source}")
            if len(matches) > 1:
                raise ValueError("More than one sound tag found.")

            self.basename = matches.pop()
        else:
            raise TypeError(f"Unsupported type. {source}")

    def __str__(self) -> str:
        return f"[sound:{self.basename}]"

    def to_path(self) -> Path:
        return Path(mw.col.media.dir()) / self.basename
