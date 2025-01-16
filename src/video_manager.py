import os
import sys


def resolve_dependencies() -> None:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../libs', 'moviepy'))
    os.environ["IMAGEIO_FFMPEG_EXE"] = os.path.join(os.path.dirname(__file__), '../libs', 'ffmpeg', 'ffmpeg')


resolve_dependencies()

from moviepy import VideoFileClip


def extract_audio(video_path: str) -> str:
    video = VideoFileClip(video_path)
    audio = video.audio

    audio_path = video_path.replace('.mp4', '.mp3')
    audio.write_audiofile(audio_path, logger=None)

    audio.close()
    video.close()

    return audio_path


def convert_to_mp4(video_path):
    video = VideoFileClip(video_path)

    mp4_path = os.path.splitext(video_path)[0] + '.mp4'
    video.write_videofile(mp4_path, codec="libx264", audio_codec="libvorbis")

    video.close()

    return mp4_path
