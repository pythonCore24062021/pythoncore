#5. Користувач робить внесок в розмірі n гривень строком на years років під 10% річних
#(щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу,
#і на них в наступному році теж будуть відсотки). Написати функцію bank, яка приймає аргументи n і years,
#і повертає суму, яка буде на рахунку користувача.

def bank(n, years):
    future_value = n * ((1 + (0.01 * 10)) ** years)
    print(round(future_value, 2))


n = int(input("enter original sum of money "))
years = int(input("enter year "))
print(bank(n,years))


