import os
import sys
from pathlib import Path


def resolve_dependencies() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))

    whisper_path = os.path.join(current_dir, '../../libs', 'whisper')
    ffmpeg_path = os.path.join(current_dir, '../../libs', 'ffmpeg', 'ffmpeg')

    if whisper_path not in sys.path:
        sys.path.append(whisper_path)

    if ffmpeg_path not in os.environ['PATH']:
        os.environ['PATH'] += f':{os.path.dirname(ffmpeg_path)}'


resolve_dependencies()

import whisper

from .stt_constants import SttWhisperArgumentsKey


class WhisperService:
    def __init__(self, config):
        self.config = config

    def transcribe(self, audio_path: Path) -> str:
        model = whisper.load_model(self.config[SttWhisperArgumentsKey.MODEL])

        result = model.transcribe(audio_path, fp16=False)

        return result["text"]
