import os
from abc import abstractmethod
from typing import Set

from aqt import mw
from aqt.editor import Editor

from ..core.constants import FieldKey
from ..core.exception import AnkidiaError
from ..core.utils import has_text, to_anki_media_path, to_sound_tag
from ..service.ffmpeg_service import convert_to_mp4, extract_audio
from ..service.html_service import build_audio_html
from ..service.whisper_service import speech_to_text


class EditorButton:
    def __init__(self, field_keys: Set[FieldKey], icon_path: str, cmd: str, tip: str):
        self.field_keys = field_keys
        self.icon_path = icon_path
        self.cmd = cmd
        self.tip = tip

    def on_click(self, editor: Editor):
        self.validate_field(editor)

        self.operate(editor)

        # Redraw editor see more https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
        editor.set_note(editor.note)

    def validate_field(self, editor):
        for field_key in self.field_keys:
            field_name = self.get_field_name(field_key)

            if not field_name in editor.note:
                raise AnkidiaError(f"Field '{field_name}' doesn't exist in the note.")

    @abstractmethod
    def operate(self, editor):
        pass

    def get_field_name(self, field_key: FieldKey):
        if field_key not in self.field_keys:
            raise AnkidiaError(f"Field '{field_key}' is not allowed.")

        config = mw.addonManager.getConfig(__name__)

        return config[field_key.value]


class ExtractAudioButton(EditorButton):
    def __init__(self):
        super().__init__(
            field_keys={FieldKey.VIDEO_FIELD, FieldKey.AUDIO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "extract_audio_icon.svg"),
            cmd="Extract audio from video",
            tip="Extract audio from video and insert into field",
        )

    def operate(self, editor: Editor):
        video_field_name = self.get_field_name(FieldKey.VIDEO_FIELD)
        video_field_value = editor.note[video_field_name]

        if not has_text(video_field_value):
            raise AnkidiaError(f"'{video_field_name}' field is empty.")

        video_path = to_anki_media_path(video_field_value)

        audio_path = extract_audio(video_path)

        audio_field_name = self.get_field_name(FieldKey.AUDIO_FIELD)
        editor.note[audio_field_name] = to_sound_tag(audio_path)


class ConvertVideoFormatButton(EditorButton):
    def __init__(self):
        super().__init__(
            field_keys={FieldKey.VIDEO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "convert_mp4_icon.svg"),
            cmd="Convert video to mp4",
            tip="Convert video to mp4",
        )

    def operate(self, editor: Editor):
        video_field_name = self.get_field_name(FieldKey.VIDEO_FIELD)
        video_field_value = editor.note[video_field_name]

        if not has_text(video_field_value):
            raise AnkidiaError(f"'{video_field_name}' field is empty.")

        video_path = to_anki_media_path(video_field_value)

        mp4_path = convert_to_mp4(video_path)

        editor.note[video_field_name] = to_sound_tag(mp4_path)


class EmbedMediaButton(EditorButton):
    def __init__(self):
        super().__init__(
            field_keys={FieldKey.AUDIO_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "embed_media_icon.svg"),
            cmd="Embed media",
            tip="Embed audio or video into field",
        )

    def operate(self, editor: Editor):
        audio_field_name = self.get_field_name(FieldKey.AUDIO_FIELD)
        audio_field_value = editor.note[audio_field_name]

        if not has_text(audio_field_value):
            raise AnkidiaError(f"'{audio_field_name}' field is empty.")

        audio_path = to_anki_media_path(audio_field_value)

        editor.note[audio_field_name] = build_audio_html(audio_path)


class SttButton(EditorButton):
    def __init__(self):
        super().__init__(
            field_keys={FieldKey.AUDIO_FIELD, FieldKey.STT_FIELD},
            icon_path=os.path.join(os.path.dirname(__file__), "../assets", "stt_icon.svg"),
            cmd="Speech to text",
            tip="Convert audio to text",
        )

    def operate(self, editor: Editor):
        audio_field_name = self.get_field_name(FieldKey.AUDIO_FIELD)
        audio_field_value = editor.note[audio_field_name]

        if not has_text(audio_field_value):
            raise AnkidiaError(f"'{audio_field_name}' field is empty.")

        audio_path = to_anki_media_path(audio_field_value)

        transcription = speech_to_text(audio_path)

        stt_field = self.get_field_name(FieldKey.STT_FIELD)
        editor.note[stt_field] = transcription
