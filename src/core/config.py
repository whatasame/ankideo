from typing import Any

from aqt import mw

from .constants import JsonKey


class Config:
    def __init__(self):
        self.config = mw.addonManager.getConfig(__name__)

    def get(self, key: JsonKey) -> Any:
        path = key.get_full_path()

        current = self.config

        for p in path:
            current = current[p]

        return current

    def set(self, key: JsonKey, value: Any):
        path = key.get_full_path()

        current = self.config
        for p in path[:-1]:
            current = current[p]

        current[path[-1]] = value

    def save(self):
        mw.addonManager.writeConfig(__name__, self.config)
