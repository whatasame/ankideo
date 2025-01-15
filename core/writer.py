from aqt.editor import Editor


def write_field(editor: Editor, target_field, value):
    note = editor.note

    note[target_field] = value

    # redraw the editor. see more https://github.com/ankitects/anki/blob/5ef2328ea4fee706599dfdbcfe9edd7856f8de9b/qt/aqt/editor.py#L111C1-L118C8
    editor.set_note(note)

