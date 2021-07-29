# task6

import random

list1 = []
list2 = []
for i in range(20):
    list1.append(int(random.randint(0, 100)))
print(f"the original list is {list1}")

for i in list1:
    if i % 2 == 0:
        list2.append(list1.index(i))
print(f"the list with positive indexes of the list1 is {list2}")
