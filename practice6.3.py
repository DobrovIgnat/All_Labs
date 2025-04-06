def is_magic_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))#разделение на день мясяц и год

        if year < 1000 or year > 9999: #проверка на 4х значность
            return False

        last_two_digits_of_year = year % 100

        return (day * month) == last_two_digits_of_year

    except ValueError:
        return False

user_input = input("Введите дату в формате dd.mm.yyyy: ")
if is_magic_date(user_input):
    print("Дата является магической!")
else:
    print("Дата не является магической.")
