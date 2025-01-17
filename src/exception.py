import sys

from aqt.utils import tooltip


class AnkidiaError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

        self.message = message


def ankidia_exception_handler(exctype, value, traceback):
    if isinstance(value, AnkidiaError):
        tooltip(value.message)
    else:
        sys.__excepthook__(exctype, value, traceback)


def init_exception_handler():
    sys.excepthook = ankidia_exception_handler
