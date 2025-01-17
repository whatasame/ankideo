import os.path

from .utils import check_file_exist


def build_audio_html(audio_path: str) -> str:
    check_file_exist(audio_path)

    basename = os.path.basename(audio_path)
    extension = os.path.splitext(basename)[1][1:]

    return f"""
<audio autoplay controls>
    <source src="{basename}" type="audio/{extension}">
    Your browser does not support the audio element.
</audio>
            """.strip()
