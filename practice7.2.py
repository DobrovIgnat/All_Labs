from collections import Counter

my_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 7]
counter = Counter(my_list)
duplicates = [item for item, count in counter.items() if count > 1]

if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Дубликатов нет.")