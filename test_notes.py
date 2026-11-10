from notes import load_notes

def test_load_notes_missing_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert load_notes() == []