# Task4
import random


def season(month):
    if month == 12 or month >= 1 and month < 3:
        return print(f"{month} - its a winter")
    elif month > 2 and month < 6:
        return print(f"{month} - its a spring")
    elif month > 5 and month < 9:
        return print(f"{month} - its a summer")
    elif month > 8 and month < 12:
        return print(f"{month} - its an autumn")
    else:
        print(f"{month} is not a year's month")


season(random.randint(0, 15))
