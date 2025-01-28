import os
import uuid
from abc import abstractmethod
from typing import List

from ..constants.convert_video_key import ConvertVideoFFmpegArgumentsKey
from ..constants.extract_audio_key import ExtractAudioFFmpegArgumentsKey
from ..core.config import Config


class FFmpegCommand:
    """
    Represents an FFmpeg command to be executed

    Output path is generated by using UUID as the filename and extension from the config
    """

    def __init__(self, input_path: str):
        self.ffmpeg_path = os.path.join(os.path.dirname(__file__), "../../libs", "ffmpeg", "ffmpeg")
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


class ConvertVideoFFmpegCommand(FFmpegCommand):

    def __init__(self, input_path: str, config: Config):
        super().__init__(input_path)

        self.config = config

    def _get_output_extension(self) -> str:
        return self.config[ConvertVideoFFmpegArgumentsKey.EXTENSION]

    def _get_ffmpeg_global_options(self) -> List[str]:
        return [
            "-y"  # overwrite output files
        ]

    def _get_ffmpeg_input_options(self) -> List[str]:
        return [

        ]

    def _get_ffmpeg_output_options(self) -> List[str]:
        video_codec = {
            "mp4": "libx264",
            "webm": "libvpx-vp9"
        }.get(self.config[ConvertVideoFFmpegArgumentsKey.EXTENSION])
        audio_codec = {
            "mp4": "aac",
            "webm": "libopus"
        }.get(self.config[ConvertVideoFFmpegArgumentsKey.EXTENSION])

        return [
            "-vf",
            f"scale={self.config[ConvertVideoFFmpegArgumentsKey.WIDTH]}:{self.config[ConvertVideoFFmpegArgumentsKey.HEIGHT]}",
            "-c:v", video_codec,
            "-crf", f"{self.config[ConvertVideoFFmpegArgumentsKey.CRF]}",
            "-c:a", audio_codec,
            "-b:a", f"{self.config[ConvertVideoFFmpegArgumentsKey.AUDIO_BITRATE]}",
            "-movflags", "faststart"
        ]


class ExtractAudioFFmpegCommand(FFmpegCommand):

    def __init__(self, input_path: str, config: Config):
        super().__init__(input_path)

        self.config = config

    def _get_output_extension(self) -> str:
        return self.config[ExtractAudioFFmpegArgumentsKey.EXTENSION]

    def _get_ffmpeg_global_options(self) -> List[str]:
        return [
            "-y"  # overwrite output files
        ]

    def _get_ffmpeg_input_options(self) -> List[str]:
        return [

        ]

    def _get_ffmpeg_output_options(self) -> List[str]:
        audio_codec = {
            "mp3": "libmp3lame",
        }.get(self.config[ExtractAudioFFmpegArgumentsKey.EXTENSION])

        return [
            "-vn",  # Ignore video
            "-acodec", audio_codec,
            "-ar", "44100",  # Audio sample rate
            "-ac", "2",  # Audio channels
            "-ab", "192k"  # Audio bitrate
        ]


class Mp4FFmpegCommand(FFmpegCommand):

    def __init__(self, input_path: str):
        super().__init__(input_path)

    def _get_output_extension(self) -> str:
        return "mp4"

    def _get_ffmpeg_global_options(self) -> List[str]:
        return [
            "-y"  # overwrite output files
        ]

    def _get_ffmpeg_input_options(self) -> List[str]:
        return [

        ]

    def _get_ffmpeg_output_options(self) -> List[str]:
        return [
            "-c:v", "libx264",
            "-crf", "30",
            "-c:a", "aac",
            "-b:a", "192k",
        ]


class WebmFFmpegCommand(FFmpegCommand):

    def __init__(self, input_path: str):
        super().__init__(input_path)

    def _get_output_extension(self) -> str:
        return "webm"

    def _get_ffmpeg_global_options(self) -> List[str]:
        return [
            "-y"  # overwrite output files
        ]

    def _get_ffmpeg_input_options(self) -> List[str]:
        return [

        ]

    def _get_ffmpeg_output_options(self) -> List[str]:
        return [
            "-c:v", "libvpx-vp9",
            "-crf", "30",
            "-c:a", "libopus",
            "-b:a", "128k"
        ]
