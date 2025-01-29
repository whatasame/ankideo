import os
import uuid
from abc import abstractmethod
from typing import List


class FFmpegCommand:
    """
    Represents an FFmpeg command to be executed

    Output path is generated by using UUID as the filename and extension from the config
    """

    def __init__(self, input_path: str):
        self.ffmpeg_path = os.path.join(os.path.dirname(__file__), "../../../libs", "ffmpeg", "ffmpeg")
        self.input_path = input_path
        self._output_path = None

    @property
    def output_path(self):
        """
        lazy load output path
        """
        if self._output_path is None:
            self._output_path = os.path.join(os.path.dirname(self.input_path),
                                             f"{uuid.uuid4()}.{self._get_output_extension()}")

        return self._output_path

    @abstractmethod
    def _get_output_extension(self) -> str:
        pass

    @abstractmethod
    def _get_ffmpeg_global_options(self) -> List[str]:
        pass

    @abstractmethod
    def _get_ffmpeg_input_options(self) -> List[str]:
        pass

    @abstractmethod
    def _get_ffmpeg_output_options(self) -> List[str]:
        pass

    def to_full_command(self) -> List[str]:
        """
        :return: the full FFmpeg command as a string list
        """
        return [
            self.ffmpeg_path,
            *self._get_ffmpeg_global_options(),
            *self._get_ffmpeg_input_options(),
            "-i", self.input_path,
            *self._get_ffmpeg_output_options(),
            self.output_path
        ]
