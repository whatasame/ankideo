from ..core.json_key import JsonKey


class ExtractAudioFieldsKey(JsonKey):
    VIDEO_FIELD = "video_field"
    AUDIO_FIELD = "audio_field"

    @staticmethod
    def get_key_name() -> str:
        return "extract_audio"

    def get_full_path(self) -> list[str]:
        return ["extract_audio", "fields", self.value]


class ExtractAudioFFmpegArgumentsKey(JsonKey):
    EXTENSION = "extension"
    AUDIO_BITRATE = "audio_bitrate"

    @staticmethod
    def get_key_name() -> str:
        return "ffmpeg_arguments"

    def get_full_path(self) -> list[str]:
        return ["extract_audio", "ffmpeg_arguments", self.value]
