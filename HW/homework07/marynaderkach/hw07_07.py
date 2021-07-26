def is_valid_date(year, month, day):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day_count_for_month[2] = 29
    return 1 <= month <= 12 and 1 <= day <= day_count_for_month[month]


print(is_valid_date(2020, 2, 29))
