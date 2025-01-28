from .json_key import JsonKey


class EmbedMediaFieldsKey(JsonKey):
    VIDEO_FIELD = "video_field"
    EMBEDDED_VIDEO_FIELD = "embedded_video_field"
    AUDIO_FIELD = "audio_field"
    EMBEDDED_AUDIO_FIELD = "embedded_audio_field"

    @staticmethod
    def get_key_name() -> str:
        return "embed_media"

    def get_full_path(self) -> list[str]:
        return ["embed_media", "fields", self.value]


class EmbedVideoTagAttributesKey(JsonKey):
    STYLE = "style"
    CONTROLS = "controls"
    AUTOPLAY = "autoplay"
    LOOP = "loop"
    MUTED = "muted"

    @staticmethod
    def get_key_name() -> str:
        return "video_tag_attributes"

    def get_full_path(self) -> list[str]:
        return ["embed_media", "video_tag_attributes", self.value]


class EmbedAudioTagAttributesKey(JsonKey):
    STYLE = "style"
    CONTROLS = "controls"
    AUTOPLAY = "autoplay"
    LOOP = "loop"
    MUTED = "muted"

    @staticmethod
    def get_key_name() -> str:
        return "audio_tag_attributes"

    def get_full_path(self) -> list[str]:
        return ["embed_media", "audio_tag_attributes", self.value]
