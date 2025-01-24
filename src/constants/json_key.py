from abc import abstractmethod
from enum import Enum


class JsonKey(Enum):
    @abstractmethod
    def get_full_path(self) -> list[str]:
        pass
