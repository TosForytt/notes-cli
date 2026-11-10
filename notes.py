import json
import sys

def load_notes():
    try:
        with open("notes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Файл notes.json повреждён")
        return None
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open("notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def add_note(add):
    notes = load_notes()
    if notes is None:
        notes = []
    notes.append(add)
    save_notes(notes)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Укажите команду: add или list")
    elif sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("Ошибка: укажите текст заметки после команды add")
        else:
            add_note(sys.argv[2])
    elif sys.argv[1] == "list":
        notes = load_notes()

        if notes is None:
            pass
        elif not notes:
            print("Список заметок пуст")
        else:
            for index, note in enumerate(notes, start=1):
                print(f"{index}, {note}")
    else:
        print("Неизвестная команда")