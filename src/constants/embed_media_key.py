from .json_key import JsonKey


class EmbedMediaFieldsKey(JsonKey):
    VIDEO_FIELD = "video_field"
    EMBEDDED_VIDEO_FIELD = "embedded_video_field"
    AUDIO_FIELD = "audio_field"
    EMBEDDED_AUDIO_FIELD = "embedded_audio_field"

    def get_full_path(self) -> list[str]:
        return ["embed_media", "fields", self.value]


class EmbedVideoTagAttributesKey(JsonKey):
    CONTROLS = "controls"
    AUTOPLAY = "autoplay"
    LOOP = "loop"
    MUTED = "muted"

    def get_full_path(self) -> list[str]:
        return ["embed_video_tag_attributes", self.value]


class EmbedAudioTagAttributesKey(JsonKey):
    CONTROLS = "controls"
    AUTOPLAY = "autoplay"
    LOOP = "loop"
    MUTED = "muted"

    def get_full_path(self) -> list[str]:
        return ["embed_audio_tag_attributes", self.value]
