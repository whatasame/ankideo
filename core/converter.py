import os
import sys

def resolve_dependencies() -> None:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../libs', 'moviepy'))
    os.environ["IMAGEIO_FFMPEG_EXE"] = os.path.join(os.path.dirname(__file__), '../libs', 'ffmpeg', 'ffmpeg')

resolve_dependencies()

from moviepy import VideoFileClip

def convert_mp4_to_mp3(mp4_path: str) -> None:
    video = VideoFileClip(mp4_path)
    audio = video.audio
    audio.write_audiofile(mp4_path.replace('.mp4', '.mp3'), logger=None)
    audio.close()
    video.close()
