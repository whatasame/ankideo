from typing import List

from aqt.editor import Editor

def append_convert_button(exist_buttons: List[str], editor: Editor) -> None:
    new_btn = editor.addButton(
        icon=None,
        cmd="Convert mp4 to mp3",
        func=lambda ed=editor: print("Hello, World!"),
        tip="Convert mp4 file in input field to mp3 and insert into output field",
        label="Convert",
    )

    exist_buttons.append(new_btn)
