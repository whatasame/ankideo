from typing import List, Optional


class FFmpegCommand:
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


class Mp3ConversionCommand(FFmpegCommand):
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


class Mp4ConversionCommand(FFmpegCommand):
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


class WebmConversionCommand(FFmpegCommand):
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
