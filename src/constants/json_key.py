from abc import abstractmethod
from enum import Enum


class JsonKey(Enum):
    @staticmethod
    def get_key_name() -> str:
        pass

    @abstractmethod
    def get_full_path(self) -> list[str]:
        pass
