from pathlib import Path
from typing import List

from .convert_constants import ConvertVideoFFmpegArgumentsKey
from ..core.config import Config
from ..core.ffmpeg.command import FFmpegCommand


class ConvertVideoFFmpegCommand(FFmpegCommand):

    def __init__(self, input_path: Path, config: Config) -> None:
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
