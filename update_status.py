def display_status(current_status):
    print(f"Текущий статус заметки: \"{current_status}\"\n")


def get_new_status():
    statuses = {
        1: "выполнено",
        2: "в процессе",
        3: "отложено"
    }

    print("Выберите новый статус заметки:")
    for key, value in statuses.items():
        print(f"{key}. {value}")

    while True:
        try:
            choice = int(input("\nВаш выбор: "))
            if choice in statuses:
                return statuses[choice]
            else:
                print("Пожалуйста, введите число от 1 до 3.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")


def main():
    # Изначальный статус заметки
    current_status = "в процессе"

    # Отображаем текущий статус
    display_status(current_status)

    # Получаем новый статус от пользователя
    new_status = get_new_status()

    # Обновляем статус и выводим результат
    current_status = new_status
    print(f"\nСтатус заметки успешно обновлён на: \"{current_status}\"")


if __name__ == "__main__":
    main()