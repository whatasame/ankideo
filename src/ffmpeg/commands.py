import os
import uuid
from abc import abstractmethod
from typing import List, Optional

from ..constants.convert_video_key import ConvertVideoFFmpegArgumentsKey
from ..constants.extract_audio_key import ExtractAudioFFmpegArgumentsKey
from ..core.config import Config


class FFmpegCommand:
    """
    Represents an FFmpeg command to be executed

    Output path is generated by using UUID as the filename and extension from the config
    """

    def __init__(self, input_path: str, config: Config):
        self.ffmpeg_path = os.path.join(os.path.dirname(__file__), "../../libs", "ffmpeg", "ffmpeg")
        self.input_path = input_path
        self.config = config
        self.output_path = self._build_output_path()

    def _build_output_path(self):
        return os.path.join(os.path.dirname(self.input_path), f"{uuid.uuid4()}.{self._get_output_extension()}")

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


class ConvertFFmpegCommand(FFmpegCommand):

    def __init__(self, input_path: str, config: Config):
        super().__init__(input_path, config)

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
        super().__init__(input_path, config)

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


class OldFFmpegCommand:
    def __init__(
            self,
            ffmpeg_path: str,
            input_path: str,
            output_path: str,
            global_options: Optional[List[str]] = None,
            input_options: Optional[List[str]] = None,
            output_options: Optional[List[str]] = None
    ):
        self.commands = [
            ffmpeg_path,
            *(global_options or []),
            *(input_options or []),
            "-i", input_path,
            *(output_options or []),
            output_path
        ]


class Mp3ConversionCommandOld(OldFFmpegCommand):
    """
    Concrete FFmpeg command class specialized for MP3 conversion
    """

    DEFAULT_GLOBAL_OPTIONS = [
        "-y"  # overwrite output files
    ]
    DEFAULT_INPUT_OPTIONS: List[str] = []
    DEFAULT_OUTPUT_OPTIONS = [
        "-vn",  # ignore video
        "-acodec", "libmp3lame",  # audio codec
        "-ar", "44100",  # audio sample rate
        "-ac", "2",  # audio channels
        "-ab", "128k"  # audio bitrate
    ]

    def __init__(
            self,
            ffmpeg_path: str,
            input_path: str,
            output_path: str,
            custom_global_options: Optional[List[str]] = None,
            custom_input_options: Optional[List[str]] = None,
            custom_output_options: Optional[List[str]] = None
    ):
        super().__init__(
            ffmpeg_path=ffmpeg_path,
            input_path=input_path,
            output_path=output_path,
            global_options=custom_global_options or self.DEFAULT_GLOBAL_OPTIONS,
            input_options=custom_input_options or self.DEFAULT_INPUT_OPTIONS,
            output_options=custom_output_options or self.DEFAULT_OUTPUT_OPTIONS
        )


class Mp4ConversionCommandOld(OldFFmpegCommand):
    """
    Concrete FFmpeg command class specialized for MP4 conversion
    """

    DEFAULT_GLOBAL_OPTIONS = [
        "-y"  # overwrite output files
    ]
    DEFAULT_INPUT_OPTIONS: List[str] = [

    ]
    DEFAULT_OUTPUT_OPTIONS = [
        "-vf", "scale=640:360",  # adjust video resolution to 640x360
        "-c:v", "libx264",  # video codec
        "-crf", "23",  # video quality
        "-c:a", "aac",  # audio codec
        "-b:a", "128k",  # audio bitrate
        "-movflags", "faststart"  # optimize for streaming
    ]

    def __init__(
            self,
            ffmpeg_path: str,
            input_path: str,
            output_path: str,
            custom_global_options: Optional[List[str]] = None,
            custom_input_options: Optional[List[str]] = None,
            custom_output_options: Optional[List[str]] = None
    ):
        super().__init__(
            ffmpeg_path=ffmpeg_path,
            input_path=input_path,
            output_path=output_path,
            global_options=custom_global_options or self.DEFAULT_GLOBAL_OPTIONS,
            input_options=custom_input_options or self.DEFAULT_INPUT_OPTIONS,
            output_options=custom_output_options or self.DEFAULT_OUTPUT_OPTIONS
        )


class WebmConversionCommandOld(OldFFmpegCommand):
    """
    Concrete FFmpeg command class specialized for WebM conversion
    """

    DEFAULT_GLOBAL_OPTIONS = [
        "-y"  # overwrite output files
    ]
    DEFAULT_INPUT_OPTIONS: List[str] = []
    DEFAULT_OUTPUT_OPTIONS = [
        "-vf", "scale=640:360",  # adjust video resolution to 640x360
        "-c:v", "libvpx-vp9",  # video codec
        "-crf", "23",  # video quality
        "-c:a", "libopus",  # audio codec
        "-b:a", "128k",  # audio bitrate
        "-movflags", "faststart"  # optimize for streaming
    ]

    def __init__(
            self,
            ffmpeg_path: str,
            input_path: str,
            output_path: str,
            custom_global_options: Optional[List[str]] = None,
            custom_input_options: Optional[List[str]] = None,
            custom_output_options: Optional[List[str]] = None
    ):
        super().__init__(
            ffmpeg_path=ffmpeg_path,
            input_path=input_path,
            output_path=output_path,
            global_options=custom_global_options or self.DEFAULT_GLOBAL_OPTIONS,
            input_options=custom_input_options or self.DEFAULT_INPUT_OPTIONS,
            output_options=custom_output_options or self.DEFAULT_OUTPUT_OPTIONS
        )
