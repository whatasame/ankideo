from abc import abstractmethod
from enum import Enum


class JsonKey(Enum):
    @staticmethod
    @abstractmethod
    def get_key_name() -> str:
        """
        :return: The key name of the JSON key.
        """
        pass

    @abstractmethod
    def get_full_path(self) -> list[str]:
        """
        :return: The hierarchical path of the JSON key.
        """
        pass
