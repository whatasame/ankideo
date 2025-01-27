from .json_key import JsonKey


class ExtractAudioFieldsKey(JsonKey):
    VIDEO_FIELD = "video_field"
    AUDIO_FIELD = "audio_field"

    def get_full_path(self) -> list[str]:
        return ["extract_audio", "fields", self.value]


class ExtractAudioFFmpegArgumentsKey(JsonKey):
    EXTENSION = "extension"
    AUDIO_BITRATE = "audio_bitrate"

    def get_full_path(self) -> list[str]:
        return ["extract_audio", "ffmpeg_arguments", self.value]
