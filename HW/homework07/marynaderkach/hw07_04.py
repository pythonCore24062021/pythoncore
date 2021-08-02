def season(month):
    if month < 3 or month == 12:
        return "Winter"
    elif month < 6:
        return "Spring"
    elif month < 9:
        return "Summer"
    elif month < 12:
        return "Autumn"
    else:
        return "Unknown month"


print(season(3))
