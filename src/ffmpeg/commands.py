import os
import uuid
from typing import List, Optional

from ..constants.convert_video_key import FFmpegArgumentsKey
from ..core.config import Config


class ConvertFFmpegCommand:
    def __init__(
            self,
            input_path: str,
            config: Config
    ):
        self.ffmpeg_path = os.path.join(os.path.dirname(__file__), "../../libs", "ffmpeg", "ffmpeg")
        self.input_path = input_path
        self.output_path = os.path.join(
            os.path.dirname(input_path), f"{uuid.uuid4()}.{config.get(FFmpegArgumentsKey.EXTENSION)}")
        self.config = config

    def to_full_command(self) -> List[str]:
        video_codec = {
            "mp4": "libx264",
            "webm": "libvpx-vp9"
        }.get(self.config.get(FFmpegArgumentsKey.EXTENSION))

        return [
            self.ffmpeg_path,
            "-i", self.input_path,
            "-vf", f"scale={self.config.get(FFmpegArgumentsKey.WIDTH)}:{self.config.get(FFmpegArgumentsKey.HEIGHT)}",
            "-c:v", video_codec,
            "-crf", f"{self.config.get(FFmpegArgumentsKey.CRF)}",
            "-c:a", "aac",
            "-b:a", f"{self.config.get(FFmpegArgumentsKey.AUDIO_BITRATE)}",
            "-movflags", "faststart",
            self.output_path
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
