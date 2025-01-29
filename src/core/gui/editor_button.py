from abc import abstractmethod
from typing import Set

from aqt.editor import Editor

from ..config import Config
from ..exception import AnkidiaError
from ..json_key import JsonKey


class EditorButton:
    def __init__(self, allowed_field_keys: Set[JsonKey], icon_path: str, cmd: str, tip: str):
        self.field_keys = allowed_field_keys
        self.icon_path = icon_path
        self.cmd = cmd
        self.tip = tip
        self.config = Config()

    def on_click(self, editor: Editor):
        self.config = Config()  # Refresh config

        self._validate_field(editor)

        self.operate(editor)

    def _validate_field(self, editor):
        """
        Validate if the fields are existed in the note
        """
        for field_key in self.field_keys:
            field_name = self.config[field_key]

            if not field_name in editor.note:
                raise AnkidiaError(f"Field '{field_name}' doesn't exist in the note.")

    @abstractmethod
    def operate(self, editor):
        pass

    def _redraw_note(self, editor):
        """
        If you want to redraw note after click, you should give them a callback function
        including redraw function. Because asynchronous operation results after operate function ends.

        And see more below why this function is needed.
        https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
        """
        editor.set_note(editor.note)

    def _get_selected_field_name(self, editor: Editor) -> str:
        """
        :return: Returns the name of the current selected field that cursor is on in the editor
        """
        current_field_index = editor.currentField
        if current_field_index is None:
            raise AnkidiaError("Click media field to embed")

        current_field_name = editor.note.keys()[current_field_index]

        return current_field_name
