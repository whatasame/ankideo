from ..core.json_key import JsonKey


class SttFieldsKey(JsonKey):
    AUDIO_FIELD = "audio_field"
    STT_FIELD = "stt_field"

    @staticmethod
    def get_key_name() -> str:
        return "stt"

    def get_full_path(self) -> list[str]:
        return ["stt", "fields", self.value]


class SttWhisperArgumentsKey(JsonKey):
    MODEL = "model"

    @staticmethod
    def get_key_name() -> str:
        return "whisper_arguments"

    def get_full_path(self) -> list[str]:
        return ["stt", "whisper_arguments", self.value]
