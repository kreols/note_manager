from datetime import datetime


def create_note():
    # Запрашиваем данные у пользователя
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")

    # Запрашиваем дату создания и дедлайн с проверкой формата
    while True:
        try:
            created_date = input("Введите дату создания (день-месяц-год): ")
            created_date = datetime.strptime(created_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Ошибка: Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")

    while True:
        try:
            deadline = input("Введите дедлайн (день-месяц-год): ")
            deadline = datetime.strptime(deadline, "%d-%m-%Y")
            break
        except ValueError:
            print("Ошибка: Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")

    # Создаём словарь с данными заметки
    note = {
        "Имя": username,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": created_date.strftime("%d-%m-%Y"),
        "Дедлайн": deadline.strftime("%d-%m-%Y")
    }

    return note


def display_notes(notes):
    # Выводим список всех заметок
    print("\nСписок заметок:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. Имя: {note['Имя']}")
        print(f"   Заголовок: {note['Заголовок']}")
        print(f"   Описание: {note['Описание']}")
        print(f"   Статус: {note['Статус']}")
        print(f"   Дата создания: {note['Дата создания']}")
        print(f"   Дедлайн: {note['Дедлайн']}\n")


def main():
    notes = []  # Список для хранения заметок

    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.\n')

    while True:
        # Создаём новую заметку
        note = create_note()
        notes.append(note)  # Добавляем заметку в список

        # Спрашиваем, хочет ли пользователь добавить ещё одну заметку
        choice = input("Хотите добавить ещё одну заметку? (да/нет): ").lower()
        if choice != "да":
            break

    # Выводим все заметки
    display_notes(notes)


if __name__ == "__main__":
    main()