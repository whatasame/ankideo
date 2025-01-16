import os
import subprocess


def convert_to_mp4(video_path: str) -> str:
    mp4_path = video_path.replace('.webm', '.mp4')

    ffmpeg_path = os.path.join(os.path.dirname(__file__), "../libs", "ffmpeg", "ffmpeg")

    command = [
        ffmpeg_path,
        "-i", video_path,
        "-c:v", "libx264",
        "-c:a", "aac",
        mp4_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 결과 확인
    if result.returncode != 0:
        print("Error:", result.stderr.decode('utf-8'))
    else:
        print("Conversion completed:", mp4_path)

    return mp4_path
