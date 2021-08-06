'''
2. Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає
    - True, якщо рік високосний, і 
    - False в іншому випадку.
'''

def is_year_leap(year):
    try:
        year = int(year)
    except ValueError:
        return "Year must be a nubmer"

    return True if year % 4 == 0 else False

for year in range (2000, 2021):
    print(f"is_year_leap({year}) = {is_year_leap(year)}")

print(f"{is_year_leap('2020') = }")
print(f"{is_year_leap('text') = }")