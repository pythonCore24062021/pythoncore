# Task3

import random

list1 = []
start = 0
end = 20
while start < end:
    list1.append(int(random.randint(-5, 4)))
    start +=1
a = 0
b = 0
for i in list1:
    if i < 0:
        a +=1
    else:
        b +=1
print(f"{list1=}")
print(f"the amount of int < 0 is {a}")
print(f"the amount of int >= 0 is {b}")
