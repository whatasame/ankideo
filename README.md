# Ankidia

Ankidia is an add-on for Anki that allows you to edit media just one click.

> [!WARNING]
> This add-on is in the early stages of development.
>
> Some features might take a long time to process and produce poor quality by ffmpeg args.
>
> Please report any issues you encounter.

## Features

* [Extract audio from video](./resources/demo_extract_audio.gif)
* Convert video to mp4 format
* [Embed media](./docs/embed-media.md)
* STT (Speech to Text) using OpenAI's Whisper

## Getting started

1. Download ffmpeg binary (specific to your OS) and move it to the `libs/ffmpeg` directory.
2. In Anki, go to `Tools > ankidia options` and set your video field and audio field.
3. Upload a video file to the video field in the editor.
4. Click a button. That's all!

## Requirements

* Anki 2.1.20 or later
* ffmpeg

## Dependencies

* [openai-whisper](https://github.com/openai/whisper)

