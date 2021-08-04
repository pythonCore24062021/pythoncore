
def season(month_number):
    if month_number in (12, 1,2):
        return "winter"
    elif month_number in (3,4,5):
        return "spring"
    elif month_number in (6,7,8):
        return "summer"
    elif month_number in (9, 10, 11):
        return "autumn"
    else:
        return "unknown month"
a = int(input("enter your month "))
print(a)
print(season(a))