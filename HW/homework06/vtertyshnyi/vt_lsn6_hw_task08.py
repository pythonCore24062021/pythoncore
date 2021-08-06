'''
8. У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.
'''

from vt_helper import get_random_list

my_list = get_random_list(5)
print(f"{my_list = }")

# get min and max elements indexes 
min_index = my_list.index(min(my_list))
max_index = my_list.index(max(my_list))

# swap elements
my_list[min_index], my_list[max_index] = my_list[max_index], my_list[min_index] 

# display results:
print(f"{my_list = }")
