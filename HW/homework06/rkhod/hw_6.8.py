# Task8

import random

list1 = []
for i in range(10):
    list1.append(int(random.randint(13, 55)))
print(f"the original list is {list1}")
mx = list1.index(max(list1))
mn = list1.index(min(list1))
list1[mx], list1[mn] = list1[mn], list1[mx]
print(f"the modified list is {list1}")

# why it not work? list1[list1.index(max(list1))], list1[list1.index(min(list1))] = list1[list1.index(min(list1))], list1[list1.index(max(list1))]
