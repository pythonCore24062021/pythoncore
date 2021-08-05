'''
4. Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12), 
   і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).
'''

def seasons(month):
    try:
        month = int(month)
        if month < 1 or month > 12:
            raise Exception("Out of range - value must be in the [1; 12]!")
    except ValueError:
        return "Parameter must be a number"
    except Exception as msg:
        return msg
    
    seasons_array = {
        'winter': (1, 2, 12),
        'spring': (3, 4, 5),
        'summerd': (6, 7, 8),
        'autmn': (9, 10, 11)
    }

    for key, values in seasons_array.items():
        for value in values:
            if value == month:
                return key

for month in range (0, 12):
    print(f"seasons({month+1}) = {seasons(month+1)}")  

print(f"seasons(0) = {seasons(0)}")  
print(f"seasons(13) = {seasons(13)}")  
print(f"seasons('text') = {seasons('text')}")  