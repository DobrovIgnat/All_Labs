numbers = [10, 20, 30, 40, 50]

user_number = int(input("Введите число: "))

if user_number in numbers:
    message = "Поздравляю, Вы угадали число!"
else:
    message = "Нет такого числа!"

print(f"\nИсходный список: {numbers}")
print(f"Число пользователя: {user_number}")
print(message)