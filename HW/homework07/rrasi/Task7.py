#7. Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. Повернути True,
# якщо така дата є в нашому календарі, і False - в іншому випадку.

def date(day, month, year):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day_count_for_month[2] = 29
    return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
print(date(day, month, year))