def determine_seat_type(seat_number):
    if seat_number < 1 or seat_number > 54:
        return "Неверный номер места. В вагоне всего 54 места."


    if 1 <= seat_number <= 36:
        seat_location = "в купе"
    elif 37 <= seat_number <= 54:
        seat_location = "боковое"
    else:
        return "Неверный номер места."

    if seat_number % 2 == 0:
        seat_type = "верхняя полка"
    else:
        seat_type = "нижняя полка"

    return f"Место {seat_number} - {seat_type}, {seat_location}."

seat_number = int(input("Введите номер места: "))
result = determine_seat_type(seat_number)
print(result)
