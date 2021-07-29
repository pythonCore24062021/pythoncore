'''
6. Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел. 
При введенні числа 0 закінчити роботу.
'''

def get_num ():
    while True:
        try:
            num = int(input())
            break
        except ValueError:
            print("Oops... You should enter numbers only")
    return num

amount_of_nums = 0
amount_of_positive = 0

while True:
    print("Enter some number:")
    n = get_num()
    if n == 0:
        break
    amount_of_nums += 1
    if n > 0:
        amount_of_positive += 1
    
if amount_of_positive != 0:
    positive = int(round((amount_of_positive/amount_of_nums)*100))
else:
    positive = 0

print(f"відсоток додатних: {positive}\
    \nвідсоток від’ємних: {100-positive}")\
    if amount_of_nums !=0 else print("There is nothing to count")
