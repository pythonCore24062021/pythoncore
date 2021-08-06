# Task 2
import random


def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f"{year} leap - ", True
    else:
        return f"{year} leap - ", False


print(is_year_leap(random.randint(1715, 2050)))
