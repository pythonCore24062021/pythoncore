'''
6. У другому списку зберегти індекси парних елементів першого списку. 
   Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2, 
   то  другий треба заповнити значеннями 1, 4, 5, 6 
   (або 0, 3, 4, 5 - якщо індексація починається з нуля), 
   оскільки саме в цих позиціях першого масиву стоять парні числа.
'''

from vt_helper import get_random_list

first_list = get_random_list(10)

second_list = [
    index
    for index, item in enumerate(first_list)
    if item % 2 == 0
]

print(f"{first_list = }")
print(f"{second_list = }")
