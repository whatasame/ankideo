from ..constants.json_key import JsonKey


class ExtractAudioFieldsKey(JsonKey):
    VIDEO_FIELD = "video_field"
    AUDIO_FIELD = "audio_field"

    def get_full_path(self) -> list[str]:
        return ["extract_audio", "fields", self.value]


class ExtractAudioFFmpegArgumentsKey(JsonKey):
    EXTENSION = "extension"

    def get_full_path(self) -> list[str]:
        return ["extract_audio", "ffmpeg_arguments", self.value]
