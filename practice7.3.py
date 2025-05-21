days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

num_weekends = int(input("Сколько выходных дней на неделе вы хотите? "))

if num_weekends < 0 or num_weekends > 7:
    print("Ошибка! Введите число от 0 до 7.")
else:
    weekend_days = list(days_of_week[-num_weekends:]) if num_weekends > 0 else []
    work_days = list(days_of_week[:-num_weekends]) if num_weekends < 7 else []

    print("\nВаши выходные дни:", ", ".join(weekend_days) if weekend_days else "Нет выходных")
    print("Ваши рабочие дни:", ", ".join(work_days) if work_days else "Нет рабочих дней")