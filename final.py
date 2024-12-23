username = input("Введите имя автора задачи ")
title = input("Введите название задачи ")
content = input("Введите описание задачи ")
status = input("Введите статус задачи ")
created_date = input("Введите дату создания задачи ")
issue_date = input("Введите дату окончания задачи ")
title_1 = input("1 Подзаголовок ")
title_2 = input("2 Подзаголовок ")
task = ["Имя пользователя - " + username, "Название - " + content, "Статус - " + status, "Начало - " + created_date,
        "Конец - " + issue_date]

print(task)
