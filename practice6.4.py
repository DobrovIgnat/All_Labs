def is_lucky_ticket(ticket_number):

    if len(ticket_number) % 2 != 0:    # Проверяем, что длина номера четная
        return False


    half_length = len(ticket_number) // 2     # Определяем длину половины


    first_half = ticket_number[:half_length]    #срез строки. Все числа до и все числа после половины
    second_half = ticket_number[half_length:]


    sum_first_half = sum(int(digit) for digit in first_half)     # Считаем суммы в каждой половине
    sum_second_half = sum(int(digit) for digit in second_half)

    return sum_first_half == sum_second_half

ticket = input("Введите номер билета: ")
if is_lucky_ticket(ticket):
    print("Билет счастливый!")
else:
    print("Билет не является счастливым.")
