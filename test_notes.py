from notes import load_notes, save_notes, add_note

def test_load_notes_missing_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert load_notes() == []

def test_save_notes_creates_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    save_notes(["арбуз"])
    assert load_notes() == ["арбуз"]

def test_add_note_appends(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    save_notes(["первая"])
    add_note("вторая")
    assert load_notes() == ["первая", "вторая"]