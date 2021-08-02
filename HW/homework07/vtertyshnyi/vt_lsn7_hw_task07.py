'''
7. Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. 
   Повернути True, якщо така дата є в нашому календарі, і False - в іншому випадку.
'''

def is_year_leap(year):
    try:
        year = int(year)
    except ValueError:
        return "Year must be a nubmer"

    return True if year % 4 == 0 else False

def date(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return "Parameters must be nubmers"

    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if year > 0:
        if month > 0 and month < 13:
            if day > 0 and day <= days_in_month.get(month):
                return True
            elif is_year_leap(year) and month == 2 and day <= 29:
                return True
            else: return False
        else: return False
    else: return False

print(f"{date(1,1,1700) = }")
print(f"{date(29,2,2010) = }")
print(f"{date(29,2,2012) = }")
print(f"{date(31,12,2019) = }")
print(f"{date(31,6,2020) = }")
print(f"{date(29,'text',2010) = }")
