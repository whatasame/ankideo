from .json_key import JsonKey


class ConvertVideoFieldsKey(JsonKey):
    VIDEO_FIELD = "video_field"

    def get_full_path(self) -> list[str]:
        return ["convert_video", "fields", self.value]


class ConvertVideoFFmpegArgumentsKey(JsonKey):
    WIDTH = "width"
    HEIGHT = "height"
    CRF = "crf"
    EXTENSION = "extension"
    AUDIO_BITRATE = "audio_bitrate"

    def get_full_path(self) -> list[str]:
        return ["convert_video", "ffmpeg_arguments", self.value]
