N = int(input("Введите количество слов: "))
words = []

for i in range(N):
    word = input(f"Введите слово {i + 1}: ")
    words.append(word)  # Добавляем слово в список

result = ' '.join(words) #в одну строку, разделяя пробелами
print("Результат:", result)
