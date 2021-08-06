'''
1. Заповнити:
    - один список випадковими числами;
    - інший - введеними з клавіатури числами;
    - в третій записати суми відповідних елементів перших двох. 
  Вивести вміст списків на екран.
'''

from vt_helper import get_user_input_numbers
from random import randint

# set the length of the lists below
list_len = 3

# populate first list with random items:
list1 = [randint(0, 100) for i in range(list_len)]

# populate second list with user inputs:
list2 = []
while len(list2) < list_len:
    print("some inputs are required, please enter a number:")
    list2.append(get_user_input_numbers())

# populate the third list with sum of the appropirate elements of the two previous lists
list3 = [list1[i] + list2[i] for i in range(list_len)]

# display results:
print(f"{list1 = }")
print(f"{list2 = }")
print(f"{list3 = }")
