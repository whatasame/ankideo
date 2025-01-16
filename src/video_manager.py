import os
import subprocess


def extract_audio(video_path: str) -> str:
    audio_path = video_path.replace('.mp4', '.mp3')

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
    mp4_path = video_path.replace('.webm', '.mp4')

    ffmpeg_path = os.path.join(os.path.dirname(__file__), "../libs", "ffmpeg", "ffmpeg")

    command = [
        ffmpeg_path,
        "-y",
        "-i", video_path,
        "-c:v", "libx264",
        "-c:a", "aac",
        mp4_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise Exception(f"Error: {result.stderr.decode('utf-8')}")

    return mp4_path
