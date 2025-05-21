countries = {
    'Россия': 'Москва',
    'Германия': 'Берлин',
    'Франция': 'Париж',
    'Италия': 'Рим',
    'Великобритания': 'Лондон',
    'Китай': 'Пекин',
    'Япония': 'Токио',
    'США': 'Вашингтон',
    'Польша': 'Варшава',
}

print("Все страны и их столицы:")
for country, capital in countries.items():
    print(f"{country}: {capital}")

selected_country = 'Франция'
print(f"\nСтолица страны {selected_country}: {countries.get(selected_country, 'Страна не найдена')}")

print("\nСловарь, отсортированный по названиям стран:") #по алфавиту
for country in sorted(countries.keys()):
    print(f"{country}: {countries[country]}")