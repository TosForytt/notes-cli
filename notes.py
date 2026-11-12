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


def add_note(text):
    notes = load_notes()
    if notes is None:
        return
    notes.append(text)
    save_notes(notes)


def delete_note(index):
    notes = load_notes()
    if notes is None:
        return
    if not notes:
        print("Список заметок пуст")
        return
    if index < 1 or index > len(notes):
        print("Ошибка: заметки с таким номером не существует")
        return

    removed = notes.pop(index - 1)
    save_notes(notes)
    print(f"Удалена заметка: {removed}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Укажите команду: add, list или delete")
    elif sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("Ошибка: укажите текст заметки после команды add")
        else:
            add_note(sys.argv[2])
    elif sys.argv[1] == "list":
        notes = load_notes()
        if notes is None:
            sys.exit()
        if not notes:
            print("Список заметок пуст")
        else:
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note}")
    elif sys.argv[1] == "delete":
        if len(sys.argv) < 3:
            print("Ошибка: укажите номер заметки после команды delete")
        elif not sys.argv[2].isdigit():
            print("Ошибка: номер заметки должен быть числом")
        else:
            delete_note(int(sys.argv[2]))
    else:
        print("Неизвестная команда")