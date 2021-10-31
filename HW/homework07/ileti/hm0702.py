# Написати функцію is_year_leap,
# приймає 1 аргумент - рік, і повертає True, якщо рік високосний,
# і False в іншому випадку.

def is_year_leap(year):
    leap  = False
    if year % 4 ==0 and year % 100 != 0:
        leap  = True
    elif year % 400 == 0:
        leap = True
    return leap
year = int(input("Leap Year: "))
print(year)
print(is_year_leap(year))

