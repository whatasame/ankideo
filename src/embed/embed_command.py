from typing import List

from ..core.ffmpeg.command import FFmpegCommand


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
            "-crf", "23",
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "faststart"
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
            "-crf", "23",
            "-c:a", "libopus",
            "-b:a", "192k",
            "-movflags", "faststart"
        ]
