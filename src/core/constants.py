from enum import Enum


class FieldKey(Enum):
    VIDEO_FIELD = "video_field"
    EMBEDDED_VIDEO_FIELD = "embedded_video_field"
    AUDIO_FIELD = "audio_field"
    EMBEDDED_AUDIO_FIELD = "embedded_audio_field"
    STT_FIELD = "stt_field"


class SupportedVideoExtension(Enum):
    MAC = "webm"
    IOS = "mp4"
