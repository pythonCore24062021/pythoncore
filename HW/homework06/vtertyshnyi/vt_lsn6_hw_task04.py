'''
4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: 
    - в один помістити тільки додатні, 
    - у другий - тільки від’ємні. 
    - Числа, рівні нулю, ігнорувати. 
   Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
'''

from vt_helper import get_random_list

my_list = get_random_list(20, -5, 5)

# create new lists based on the list above:
pos_items = [item for item in my_list if item > 0]
neg_items = [item for item in my_list if item < 0]

# display results:
print(f"{my_list = }")
print(f"{pos_items = }")
print(f"{neg_items = }")
