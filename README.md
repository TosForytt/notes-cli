# Программа для заметок

## Требования
Python 3.14.4
requirements.txt - перечислены зависимости

## Установка
Linux / MacOS:
установка .venv - `python3 -m venv .venv`
активация .venv - `source .venv/bin/activate`
установка зависимостей - `pip install -r requirements.txt`

Windows:
`python -m venv .venv` (если python3 не работает, попробуй python или py)
   cmd:
`.venv\Scripts\activate.bat`
   powershell:
`.\.venv\Scripts\Activate.ps1`

## Использование

запуск CLI - `python3 notes.py` (вывод: Укажите команду: add или list)
ввести свою новую заметку - `python3 notes.py add "заметка"`
показывает список заметок - `python3 notes.py list`
удалить заметку - `python3 notes.py delete 1`

## Где хранятся данные

notes.json

## Тесты

запуск теста - `pytest`
passed - все тесты прошли успешно
failed - программа работает не правильно