# Task4

import random

list1 = []
list2 = []
list3 = []

for i in range(10):
    list1.append(int(random.randint(-5, 5)))
print(f"the original list = {list1}")
for i in list1:
    if i < 0:
        list2.append(i)
    elif i > 0:
        list3.append(i)

print(f"the list where int > 0 is {list2}")
print(f"the list where int < 0 is {list3}")
