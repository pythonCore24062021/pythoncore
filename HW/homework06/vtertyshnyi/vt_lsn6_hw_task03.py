'''
3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список. 
   Порахувати кількість додатних, від’ємних і нульових елементів. 
   Вивести на екран елементи списку і пораховані кількості.
'''

from random import randint

# set the settings of the list to gerenate: length, min value, max value
list_settings = {
    'length': 20,
    'min_val': -5,
    'max_val': 4
}

# populate list with random items:
my_list = [
    randint(list_settings['min_val'], list_settings['max_val']) 
    for i in range(list_settings['length'])
    ]

# calculate amounts of pos / neg / 0 values:
amount_of_pos_items = 0
amount_of_neg_items = 0
amount_of_zero_items = 0
for item in my_list:
    if item > 0:
        amount_of_pos_items += 1
    elif item < 0:
        amount_of_neg_items += 1
    else:
        amount_of_zero_items += 1

# display results
print(f"{my_list = }")
print(f"{amount_of_pos_items = }")
print(f"{amount_of_neg_items = }")
print(f"{amount_of_zero_items = }")
