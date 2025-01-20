import os.path

from ..core.utils import check_file_exist


def build_video_html(video_paths: list[str]) -> str:
    source_tags = []
    for video_path in video_paths:
        check_file_exist(video_path)

        basename = os.path.basename(video_path)
        extension = os.path.splitext(basename)[1][1:]

        source_tags.append(f"<source src={basename} type=video/{extension}>")

    return f"""
<video controls style"max-width:100%; height: auto;">
    {''.join(source_tags)}
    Your browser does not support the video tag.
</video>
            """.strip()


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
