def a100_by_number(number):
    return 100 / number

try:
    user_input = input("Введите число для деления 100: ")
    user_number = float(user_input)  # число с плавающей точкой

    result = a100_by_number(user_number)
    print(f"100 деленное на {user_number} равно {result:.2f}")

except ValueError:
    print("Ошибка: Пожалуйста, введите корректное число.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно.")
