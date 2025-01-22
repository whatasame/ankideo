from abc import abstractmethod
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


class JsonKey(Enum):
    @staticmethod
    @abstractmethod
    def get_key_name() -> str:
        pass

    @abstractmethod
    def get_full_path(self) -> list[str]:
        pass


class EmbedMedia(JsonKey):
    VIDEO_FIELD = "video_field"
    EMBEDDED_VIDEO_FIELD = "embedded_video_field"
    AUDIO_FIELD = "audio_field"
    EMBEDDED_AUDIO_FIELD = "embedded_audio_field"

    @staticmethod
    def get_key_name() -> str:
        return "embed_media"

    def get_full_path(self) -> list[str]:
        return [self.get_key_name(), self.value]


class AudioTagAttribute(JsonKey):
    CONTROLS = "controls"
    AUTOPLAY = "autoplay"
    LOOP = "loop"
    MUTED = "muted"

    @staticmethod
    def get_key_name() -> str:
        return "audio_tag_attribute"

    def get_full_path(self) -> list[str]:
        return [EmbedMedia.get_key_name(), self.get_key_name(), self.value]


class VideoTagAttribute(JsonKey):
    CONTROLS = "controls"
    AUTOPLAY = "autoplay"
    LOOP = "loop"
    MUTED = "muted"

    @staticmethod
    def get_key_name() -> str:
        return "video_tag_attribute"

    def get_full_path(self) -> list[str]:
        return [EmbedMedia.get_key_name(), self.get_key_name(), self.value]


class ConvertVideo(JsonKey):
    TARGET_EXTENSION = "target_extension"
    FFMPEG_GLOBAL_OPTIONS = "ffmpeg_global_options"
    FFMPEG_INPUT_OPTIONS = "ffmpeg_input_options"
    FFMPEG_OUTPUT_OPTIONS = "ffmpeg_output_options"

    @staticmethod
    def get_key_name() -> str:
        return "convert_video"

    def get_full_path(self) -> list[str]:
        return [self.get_key_name(), self.value]
