words = []

print("Введите слова (введите 'stop' для завершения ввода):")

while True:
    word = input("Введите слово: ")
    if word.lower() == 'stop': #проверка на стоп
        break
    words.append(word)


result = ' '.join(words) #в одну строку, разделяя пробелами

# Выводим результат
print("Результат:", result)
