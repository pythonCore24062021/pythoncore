'''
2. Заповнити список дійсними числами введенням з клавіатури. 
   Порахувати суму і добуток елементів списку. 
   Вивести на екран сам список, отримані суму і добуток його елементів.
'''

from vt_helper import get_user_input_float

# set the length of the lists below
list_len = 3

# populate second list with user inputs:
my_list = []
while len(my_list) < list_len:
    print("some inputs are required, please enter a number:")
    my_list.append(get_user_input_float())

# calculate list multiplication
list_multiplication = 1
for item in my_list:
    list_multiplication *= item

# display results:
print(f"{my_list = }")
print(f"my_list elements sum is {sum(my_list)}")
print(f"my_list elements multiplication is {list_multiplication}")
