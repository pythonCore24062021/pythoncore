# Task7

import random

list1 = []
for i in range(10):
    list1.append(int(random.randint(0, 5)))
print(f"the original list is {list1}")
list2 = set(list1)
print(f"the list with unique elements is {list2}")
