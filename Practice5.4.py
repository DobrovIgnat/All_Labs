import random

def math_game():
    correct_answers = 0
    incorrect_answers = 0

    print("Добро пожаловать в игру 'Математика для детей'!")
    print("Вы должны решить примеры. У вас 3 попытки на ошибку.")

    while incorrect_answers < 3:
        num1 = random.randint(1, 10) #создаем рандомные 2 числа и формируем выражение
        num2 = random.randint(1, 10)

        expression = f"{num1} + {num2} = "

        try:
            user_answer = int(input(expression))
        except ValueError:
            print("Пожалуйста, введите число.")#проверка чтобы было число
            continue

        if user_answer == num1 + num2:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Ответ неверный.")
            incorrect_answers += 1

    print(f"Игра окончена. Правильных ответов: {correct_answers}")

math_game()
