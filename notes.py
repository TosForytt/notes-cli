import json

def load_notes():
    try:
        with open("notes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

print(load_notes())