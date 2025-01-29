from ..constants.embed_media_key import EmbedVideoTagAttributesKey, EmbedAudioTagAttributesKey
from ..core.utils import split_basename_and_extension


class HtmlTagFactory:
    def __init__(self, config):
        self._config = config

    def generate_video_tag(
            self,
            video_paths: list[str],
    ) -> str:
        attributes = [
            f'style="{self._config[EmbedVideoTagAttributesKey.STYLE]}"',
            'controls=""' if self._config[EmbedVideoTagAttributesKey.CONTROLS] else '',
            'autoplay=""' if self._config[EmbedVideoTagAttributesKey.AUTOPLAY] else '',
            'loop=""' if self._config[EmbedVideoTagAttributesKey.LOOP] else '',
            'muted=""' if self._config[EmbedVideoTagAttributesKey.MUTED] else '',
            'playsinline=""'
        ]

        source_tags = [self._to_source_tag(video_path) for video_path in video_paths]

        return f"""
<video {' '.join(attributes)}>
    {''.join(source_tags)}
    Your browser does not support the video tag.
</video>
        """.strip()

    def _to_source_tag(self, source_path: str) -> str:
        basename, extension = split_basename_and_extension(source_path)

        return f"<source src={basename} type=video/{extension}>"

    def generate_audio_tag(
            self,
            audio_path: str,
    ) -> str:
        attributes = [
            f'style="{self._config[EmbedAudioTagAttributesKey.STYLE]}"',
            'controls=""' if self._config[EmbedAudioTagAttributesKey.CONTROLS] else '',
            'autoplay=""' if self._config[EmbedAudioTagAttributesKey.AUTOPLAY] else '',
            'loop=""' if self._config[EmbedAudioTagAttributesKey.LOOP] else '',
            'muted=""' if self._config[EmbedAudioTagAttributesKey.MUTED] else '',
        ]

        basename, extension = split_basename_and_extension(audio_path)

        return f"""
<audio {' '.join(attributes)}>
    <source src="{basename}" type="audio/{extension}">
    Your browser does not support the audio element.
</audio>
        """.strip()
