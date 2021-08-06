'''
5. Заповнити список випадковими додатними і від’ємними цілими числами. 
   Вивести його на екран. 
   Видалити з списку всі від’ємні елементи і знову вивести.
'''

from vt_helper import get_random_list

my_list = get_random_list()
print(f"{my_list = }")

# remove negative values
my_list = [
   item 
   for item in my_list
   if item >= 0
]
print(f"{my_list = }")
