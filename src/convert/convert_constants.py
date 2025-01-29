from ..core.json_key import JsonKey


class ConvertVideoFieldsKey(JsonKey):
    VIDEO_FIELD = "video_field"

    @staticmethod
    def get_key_name() -> str:
        return "convert_video"

    def get_full_path(self) -> list[str]:
        return ["convert_video", "fields", self.value]


class ConvertVideoFFmpegArgumentsKey(JsonKey):
    WIDTH = "width"
    HEIGHT = "height"
    CRF = "crf"
    EXTENSION = "extension"
    AUDIO_BITRATE = "audio_bitrate"

    @staticmethod
    def get_key_name() -> str:
        return "ffmpeg_arguments"

    def get_full_path(self) -> list[str]:
        return ["convert_video", "ffmpeg_arguments", self.value]
