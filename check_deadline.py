from datetime import datetime

def get_current_date():
    # Получаем текущую дату
    return datetime.now()

def get_deadline_date():
    while True:
        try:
            # Запрашиваем у пользователя дату дедлайна
            deadline_str = input("Введите дату дедлайна (в формате день-месяц-год): ")
            # Преобразуем строку в объект datetime
            deadline = datetime.strptime(deadline_str, "%d-%m-%Y")
            return deadline
        except ValueError:
            print("Ошибка: Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")

def compare_dates(current_date, deadline):
    # Вычисляем разницу между текущей датой и дедлайном
    delta = deadline - current_date
    days = delta.days

    if days < 0:
        print(f"Внимание! Дедлайн истёк {abs(days)} дня(дней) назад.")
    elif days == 0:
        print("Дедлайн сегодня!")
    else:
        print(f"До дедлайна осталось {days} дня(дней).")

def main():
    # Получаем текущую дату
    current_date = get_current_date()
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}\n")

    # Получаем дату дедлайна от пользователя
    deadline = get_deadline_date()

    # Сравниваем даты и выводим результат
    compare_dates(current_date, deadline)

if __name__ == "__main__":
    main()