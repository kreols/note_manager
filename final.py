import datetime

task = {}

task["username"] = input("Введите имя автора задачи: ")
task["title"] = input("Введите название задачи: ")
task["content"] = input("Введите описание задачи: ")
task["status"] = input("Введите статус задачи: ")

#  Обработка даты создания с возможностью использования текущей даты
created_date_input = input("Введите дату создания задачи (ГГГГ-ММ-ДД) или нажмите Enter для использования текущей даты: ")
if not created_date_input:
    task["created_date"] = datetime.date.today().strftime("%Y-%m-%d")
else:
    try:
        task["created_date"] = datetime.datetime.strptime(created_date_input, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Неверный формат даты. Используется текущая дата.")
        task["created_date"] = datetime.date.today().strftime("%Y-%m-%d")


# Обработка даты окончания с возможностью использования текущей даты + 7 дней 
issue_date_input = input("Введите дату окончания задачи (ГГГГ-ММ-ДД) или нажмите Enter для использования даты через 7 дней: ")
if not issue_date_input:
    task["issue_date"] = (datetime.date.today() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
else:
    try:
        task["issue_date"] = datetime.datetime.strptime(issue_date_input, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Неверный формат даты. Используется дата через 7 дней.")
        task["issue_date"] = (datetime.date.today() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")



task["subtitles"] = [input("1 Подзаголовок: "), input("2 Подзаголовок: ")]


print(task)
