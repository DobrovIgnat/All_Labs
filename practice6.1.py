def check_3(number):
    if number % 3 == 0:
        return True
    else:
        return False

try:
    user_input = int(input("Введите число для проверки: "))
    if check_3(user_input):
        print(f"{user_input} делится на 3.")
    else:
        print(f"{user_input} не делится на 3.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
