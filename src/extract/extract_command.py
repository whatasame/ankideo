from pathlib import Path
from typing import List

from ..core.config import Config
from ..core.ffmpeg.command import FFmpegCommand
from ..extract.extract_constants import ExtractAudioFFmpegArgumentsKey


class ExtractAudioFFmpegCommand(FFmpegCommand):

    def __init__(self, input_path: Path, config: Config):
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
