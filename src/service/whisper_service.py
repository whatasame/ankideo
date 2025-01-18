import os
import sys


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

from ..core.utils import check_file_exist


def speech_to_text(audio_path: str) -> str:
    check_file_exist(audio_path)

    model = whisper.load_model("small")

    result = model.transcribe(audio_path, fp16=False)

    return result["text"]
