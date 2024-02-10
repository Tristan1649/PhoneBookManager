import json

PHONE_BOOK_FILE = "phone_book.json"

def load_phone_book() -> list:
    """
    Загружает телефонную книгу из файла и возвращает её.

    Returns:
        list: Телефонная книга, представленная в виде списка словарей.
    """
    try:
        with open(PHONE_BOOK_FILE, 'r') as file:  # Тип данных: файл
            phone_book = json.load(file)  # Тип данных: list
    except FileNotFoundError:
        phone_book = []  # Тип данных: list
    return phone_book  # Тип данных: list

def save_phone_book(phone_book: list) -> None:
    """
    Сохраняет телефонную книгу в файл.

    Args:
        phone_book (list): Телефонная книга в виде списка словарей.
    """
    with open(PHONE_BOOK_FILE, 'w') as file:  # Тип данных: файл
        json.dump(phone_book, file, indent=2)  # Тип данных: list

def display_records(records: list) -> None:
    """
    Выводит записи телефонной книги на экран.

    Args:
        records (list): Список записей телефонной книги.
    """
    for record in records:  # Тип данных: list
        print(record)  # Тип данных: dict

def add_record(phone_book: list, record: dict) -> None:
    """
    Добавляет новую запись в телефонную книгу и сохраняет изменения в файл.

    Args:
        phone_book (list): Телефонная книга в виде списка словарей.
        record (dict): Новая запись в виде словаря.
    """
    phone_book.append(record)  # Тип данных: list
    save_phone_book(phone_book)  # Тип данных: list

def edit_record(phone_book: list, index: int, new_record: dict) -> None:
    """
    Редактирует существующую запись в телефонной книге и сохраняет изменения в файл.

    Args:
        phone_book (list): Телефонная книга в виде списка словарей.
        index (int): Индекс записи, которую нужно отредактировать.
        new_record (dict): Новые данные для записи в виде словаря.
    """
    phone_book[index] = new_record  # Тип данных: list
    save_phone_book(phone_book)  # Тип данных: list

def search_records(phone_book: list, criteria: str) -> list:
    """
    Осуществляет поиск записей по заданным критериям и возвращает совпадающие записи.

    Args:
        phone_book (list): Телефонная книга в виде списка словарей.
        criteria (str): Критерий поиска.

    Returns:
        list: Список записей, соответствующих критериям поиска.
    """
    matching_records = []  # Тип данных: list
    for record in phone_book:  # Тип данных: list
        if any(value.lower() == criteria.lower() for value in record.values()):  # Тип данных: str
            matching_records.append(record)  # Тип данных: dict
    return matching_records  # Тип данных: list

def main() -> None:
    """
    Главная функция управления телефонной книгой.
    """
    phone_book = load_phone_book()  # Тип данных: list

    while True:  # Тип данных: bool
        print("\n1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("0. Выход")

        choice = input("Выберите действие: ")  # Тип данных: str

        if choice == "1":  # Тип данных: str
            display_records(phone_book)  # Тип данных: list
        elif choice == "2":  # Тип данных: str
            new_record = {
                "Фамилия": input("Введите фамилию: "),  # Тип данных: str
                "Имя": input("Введите имя: "),  # Тип данных: str
                "Отчество": input("Введите отчество: "),  # Тип данных: str
                "Организация": input("Введите название организации: "),  # Тип данных: str
                "Телефон рабочий": input("Введите рабочий телефон: "),  # Тип данных: str
                "Телефон личный": input("Введите личный телефон: "),  # Тип данных: str
            }
            add_record(phone_book, new_record)  # Тип данных: list
            print("Запись добавлена.")  # Тип данных: None
        elif choice == "3":  # Тип данных: str
            index = int(input("Введите индекс записи для редактирования: "))  # Тип данных: int
            if 0 <= index < len(phone_book):  # Тип данных: int
                new_record = {  # Тип данных: dict
                    "Фамилия": input("Введите новую фамилию: "),  # Тип данных: str
                    "Имя": input("Введите новое имя: "),  # Тип данных: str
                    "Отчество": input("Введите новое отчество: "),  # Тип данных: str
                    "Организация": input("Введите новое название организации: "),  # Тип данных: str
                    "Телефон рабочий": input("Введите новый рабочий телефон: "),  # Тип данных: str
                    "Телефон личный": input("Введите новый личный телефон: "),  # Тип данных: str
                }
                edit_record(phone_book, index, new_record)  # Тип данных: list
                print("Запись отредактирована.")  # Тип данных: None
            else:  # Тип данных: bool
                print("Неверный индекс.")  # Тип данных: None
        elif choice == "4":  # Тип данных: str
            criteria = input("Введите критерий поиска: ")  # Тип данных: str
            matching_records = search_records(phone_book, criteria)  # Тип данных: list
            if matching_records:  # Тип данных: list
                display_records(matching_records)  # Тип данных: list
            else:  # Тип данных: bool
                print("Нет совпадений.")  # Тип данных: None
        elif choice == "0":  # Тип данных: str
            break  # Тип данных: None
        else:  # Тип данных: bool
            print("Неверный выбор. Попробуйте снова.")  # Тип данных: None

if __name__ == "__main__":  # Тип данных: None
    main()  # Тип данных: None