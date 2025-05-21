group1 = ['Смирнов', 'Петров', 'Иванов', 'Кузнецов', 'Соколов', 'Васильев', 'Попов', 'Новиков', 'Федоров', 'Морозов']
group2 = ['Лебедев', 'Козлов', 'Соловьев', 'Волков', 'Зайцев', 'Павлов', 'Семенов', 'Голубев', 'Виноградов', 'Богданов']

import random
team = tuple(random.sample(group1, 5) + random.sample(group2, 5))

print("Исходный список 1-й группы:", group1)
print("Исходный список 2-й группы:", group2)
print("\nСпортивная команда:", team)

print("\nДлина кортежа команды:", len(team))

sorted_team = tuple(sorted(team))
print("\nОтсортированная команда:", sorted_team) # по алфавиту

count_ivanov = team.count('Иванов')
if count_ivanov > 0:
    print(f"\nСтудент 'Иванов' входит в команду. Количество раз: {count_ivanov}")
else:
    print("\nСтудент 'Иванов' не входит в команду.")