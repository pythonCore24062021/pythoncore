#4. Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12),
#і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).

def season(month_number):
    if month_number in (12, 1, 2):
        return "winter"
    elif month_number in (3, 4, 5):
        return "spring"
    elif month_number in (6, 7, 8):
        return "summer"
    elif month_number in (9, 10, 11):
        return "automn"
    else:
        return "unknown month"
a = int(input("enter number of month "))
print(season(a))
