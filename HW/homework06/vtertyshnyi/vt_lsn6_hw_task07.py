'''
7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран. 
'''

from vt_helper import get_random_list

my_list = get_random_list(5, 1, 6)

unique_from_my_list = [
    item
    for item in my_list
    if my_list.count(item) == 1
]

print(f"{my_list = }")
print(f"{unique_from_my_list = }")
