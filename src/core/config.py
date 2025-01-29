from typing import Any

from aqt import mw

from .json_key import JsonKey


class Config:
    """
    Wrapper class for Anki addon configuration.

    The anki config is a dictionary-like object. So to access hierarchically nested keys,
    we invoke recursively `__getitem__` method.
    """

    def __init__(self):
        self.json = mw.addonManager.getConfig(__name__)

    def __getitem__(self, key: JsonKey) -> Any:
        path = key.get_full_path()

        current = self.json

        for p in path:
            current = current[p]

        return current

    def set(self, key: JsonKey, value: Any):
        path = key.get_full_path()

        current = self.json
        for p in path[:-1]:
            current = current[p]

        current[path[-1]] = value

    def save(self):
        mw.addonManager.writeConfig(__name__, self.json)
