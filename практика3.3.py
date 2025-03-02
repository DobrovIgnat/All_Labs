year_input = int(input("Введите год: "))
if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
    print(f"Год {year_input} - високосный.")
else:
    print("Это год не високосный.")
