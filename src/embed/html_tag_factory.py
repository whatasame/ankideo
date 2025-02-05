from pathlib import Path

from .embed_constants import EmbedVideoTagAttributesKey, EmbedAudioTagAttributesKey
from ..core.config import Config


class HtmlTagFactory:
    def __init__(self, config: Config) -> None:
        self._config = config

    def generate_video_tag(
            self,
            video_paths: list[Path],
    ) -> str:
        attributes = [
            f'style="{self._config[EmbedVideoTagAttributesKey.STYLE]}"',
            'controls=""' if self._config[EmbedVideoTagAttributesKey.CONTROLS] else '',
            'autoplay=""' if self._config[EmbedVideoTagAttributesKey.AUTOPLAY] else '',
            'loop=""' if self._config[EmbedVideoTagAttributesKey.LOOP] else '',
            'muted=""' if self._config[EmbedVideoTagAttributesKey.MUTED] else '',
            'playsinline=""'
        ]

        source_tags = [f"<source src={source_path.name} type=video/{source_path.suffix.lstrip('.')}>"
                       for source_path in video_paths]

        attributes_str = ' '.join(attributes)
        source_tags_str = '\n'.join(source_tags)

        return f"""
<video {attributes_str}>
    {source_tags_str}
    Your browser does not support the video tag.
</video>
        """.strip()

    def generate_audio_tag(
            self,
            audio_path: Path,
    ) -> str:
        attributes = [
            f'style="{self._config[EmbedAudioTagAttributesKey.STYLE]}"',
            'controls=""' if self._config[EmbedAudioTagAttributesKey.CONTROLS] else '',
            'autoplay=""' if self._config[EmbedAudioTagAttributesKey.AUTOPLAY] else '',
            'loop=""' if self._config[EmbedAudioTagAttributesKey.LOOP] else '',
            'muted=""' if self._config[EmbedAudioTagAttributesKey.MUTED] else '',
        ]

        return f"""
<audio {' '.join(attributes)}>
    <source src="{audio_path.name}" type="audio/{audio_path.suffix.lstrip('.')}">
    Your browser does not support the audio element.
</audio>
        """.strip()
