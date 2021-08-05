'''
5. Користувач робить внесок в розмірі 
    - n гривень 
    - строком на years років 
    - під 10% річних 
   (щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу, 
   і на них в наступному році теж будуть відсотки).
   Написати функцію bank, яка приймає аргументи n і years, 
   і повертає суму, яка буде на рахунку користувача.
'''

def bank(amount, years):
    try:
        amount = int(amount)
        years = int(years)
        if amount < 0 or years < 0: raise Exception("Values must be positive")
    except ValueError:
        return "Parameters must be numbers"
    except Exception as msg:
        return msg

    rate = 0.1

    for year in range(years):
        amount *= (rate + 1)

    return amount

amount = 100
for year in range(-1, 4):
    print(f"bank({amount},{year}) = {bank(amount, year)}")

print(f"bank('text',{year}) = {bank('text', year)}")
print(f"bank({amount},'text') = {bank(amount, 'text')}")
amount = -100
print(f"bank({amount},{year}) = {bank(amount, year)}")