import os
import subprocess
import uuid
from typing import List

from ..core.old_constants import SupportedVideoExtension
from ..core.utils import check_file_exist
from ..ffmpeg.commands import Mp4ConversionCommandOld, WebmConversionCommandOld, Mp3ConversionCommandOld

FFMPEG_PATH = os.path.join(os.path.dirname(__file__), "../../libs", "ffmpeg", "ffmpeg")


def extract_audio(video_path: str) -> str:
    check_file_exist(video_path)

    # use uuid to avoid name conflict like percent encoding
    result_path = os.path.join(os.path.dirname(video_path), f"{uuid.uuid4()}.mp3")

    commands = Mp3ConversionCommandOld(FFMPEG_PATH, video_path, result_path).commands

    cmd_result = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if cmd_result.returncode != 0:
        raise Exception(f"Error: {cmd_result.stderr.decode('utf-8')}")

    return result_path


def convert_to_mp4(video_path: str) -> str:
    check_file_exist(video_path)

    # use uuid to avoid name conflict like percent encoding
    result_path = os.path.join(os.path.dirname(video_path), f"{uuid.uuid4()}.mp4")

    commands = Mp4ConversionCommandOld(FFMPEG_PATH, video_path, result_path).commands

    cmd_result = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if cmd_result.returncode != 0:
        raise Exception(f"Error: {cmd_result.stderr.decode('utf-8')}")

    return result_path


def convert_to_webm(video_path: str) -> str:
    check_file_exist(video_path)

    # use uuid to avoid name conflict like percent encoding
    result_path = os.path.join(os.path.dirname(video_path), f"{uuid.uuid4()}.webm")

    commands = WebmConversionCommandOld(FFMPEG_PATH, video_path, result_path).commands

    cmd_result = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if cmd_result.returncode != 0:
        raise Exception(f"Error: {cmd_result.stderr.decode('utf-8')}")

    return result_path


def convert_compatibles(video_path: str, *extensions: SupportedVideoExtension) -> List[str]:
    format_converters = {
        SupportedVideoExtension.MAC: convert_to_webm,
        SupportedVideoExtension.IOS: convert_to_mp4
    }

    return [format_converters[fmt](video_path) for fmt in extensions]
