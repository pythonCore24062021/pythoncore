# Task 7

def date(month, day, year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and 0 < day < 32:
            return True
        elif month == 2 and 0 < day < 30:
            return True
        elif month == 4 or month == 6 or month == 9 or month == 11 and 0 < day < 31:
            return True
        else:
            return False
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and 0 < day < 32:
        return True
    elif month == 2 and 0 < day < 29:
        return True
    elif month == 4 or month == 6 or month == 9 or month == 11 and 0 < day < 31:
        return True
    else:
        return False


print(date(int(input("Enter a month\t")), int(input("Enter a day\t")), int(input("Enter a year\t"))))
