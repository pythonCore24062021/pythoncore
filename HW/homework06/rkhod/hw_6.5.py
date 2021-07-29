# Task5

import random
list1 = []
for i in range(20):
    list1.append(int(random.randint(-10, 10)))
print(f"the original list = {list1}")
list1 = [i for i in list1 if i >= 0]
print(f"the modified list = {list1}")

# for i in list1:
#     if i < 0:
#         list1.remove(i)
# print(f"the modified list = {list1}")  - why this not work?
