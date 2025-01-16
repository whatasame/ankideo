import os
import subprocess
import uuid


def extract_audio(video_path: str) -> str:
    audio_path = os.path.splitext(video_path)[0] + '.mp3'

    ffmpeg_path = os.path.join(os.path.dirname(__file__), "../libs", "ffmpeg", "ffmpeg")

    command = [
        ffmpeg_path,
        '-y',
        '-i', video_path,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ar', '44100',
        '-ac', '2',
        '-ab', '128k',
        audio_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise Exception(f"Error: {result.stderr.decode('utf-8')}")

    return audio_path


def convert_to_mp4(video_path: str) -> str:
    mp4_name = f"{uuid.uuid4()}.mp4"  # use uuid to avoid name conflict like percent encoding
    mp4_path = os.path.join(os.path.dirname(video_path), mp4_name)

    ffmpeg_path = os.path.join(os.path.dirname(__file__), "../libs", "ffmpeg", "ffmpeg")

    command = [
        ffmpeg_path,
        "-y",
        "-i", video_path,
        "-vf", "scale=854:480",
        "-c:v", "libx264",
        "-b:v", "1200k",
        "-preset", "fast",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "faststart",
        mp4_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise Exception(f"Error: {result.stderr.decode('utf-8')}")

    return mp4_path
