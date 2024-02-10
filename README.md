# PhoneBookManager

## Методы:

### `load_phone_book(): list`

**Действия:**
1. Вызов метода `load_phone_book()` из `PhoneBookManager`.
2. Внутренний вызов метода `load(file)` из `JSONUtil`.
3. `JSONUtil` загружает данные из файла (тип: str) и возвращает телефонную книгу (тип: list).
4. Метод `load_phone_book()` возвращает полученную телефонную книгу.

### `save_phone_book(phone_book: list) -> None`

**Действия:**
1. Вызов метода `save_phone_book(phone_book)` из `PhoneBookManager`.
2. Внутренний вызов метода `dump(data, file)` из `JSONUtil`.
3. `JSONUtil` сохраняет телефонную книгу (тип: list) в файл (тип: str).

### `display_records(records: list) -> None`

**Действия:**
1. Вызов метода `display_records(records)` из `PhoneBookManager`.
2. Вывод записей телефонной книги на экран.

### `add_record(phone_book: list, record: dict) -> None`

**Действия:**
1. Вызов метода `add_record(phone_book, record)` из `PhoneBookManager`.
2. Добавление новой записи (тип: dict) в телефонную книгу (тип: list).

### `edit_record(phone_book: list, index: int, new_record: dict) -> None`

**Действия:**
1. Вызов метода `edit_record(phone_book, index, new_record)` из `PhoneBookManager`.
2. Редактирование существующей записи (тип: dict) в телефонной книге (тип: list).

### `search_records(phone_book: list, criteria: str) -> list`

**Действия:**
1. Вызов метода `search_records(phone_book, criteria)` из `PhoneBookManager`.
2. Осуществление поиска записей по заданным критериям (тип: str) и возврат совпадающих записей (тип: list).

### `main() -> None`

**Действия:**
1. Вызов метода `main()` из `PhoneBookManager`.
2. Управление основным циклом программы, предоставление пользователю меню действий.

# JSONUtil

## Методы:

### `load(file: str) -> list`

**Действия:**
1. Внешний вызов метода `load(file)` из `JSONUtil`.
2. Загрузка данных из файла (тип: str) и возврат телефонной книги (тип: list).

### `dump(data: list, file: str) -> None`

**Действия:**
1. Внешний вызов метода `dump(data, file)` из `JSONUtil`.
2. Сохранение телефонной книги (тип: list) в файл (тип: str).

# json (библиотека Python)

## Методы:

### `load(file: str) -> list`

**Действия:**
1. Внешний вызов метода `load(file)` из библиотеки `json`.
2. Загрузка данных из файла (тип: str) и возврат телефонной книги (тип: list).

### `dump(data: list, file: str) -> None`

**Действия:**
1. Внешний вызов метода `dump(data, file)` из библиотеки `json`.
2. Сохранение телефонной книги (тип: list) в файл (тип: str).
