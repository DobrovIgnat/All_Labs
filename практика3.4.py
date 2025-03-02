color1 = input("Введите первый основной цвет (красный, синий, желтый): ").lower() #штука в конце чекает регистр
color2 = input("Введите второй основной цвет (красный, синий, желтый): ").lower()

if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
    result_color = "фиолетовый"
elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
    result_color = "оранжевый"
elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
    result_color = "зеленый"
else:
    result_color = None

if result_color:
    print(f"Смешивание {color1} и {color2} дает {result_color}.")
else:
    print("Ошибка: введены неверные цвета. Пожалуйста, используйте 'красный', 'синий' или 'желтый'.")
