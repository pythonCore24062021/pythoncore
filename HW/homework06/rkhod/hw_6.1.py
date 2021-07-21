# Task1
import random

list1 = []
start = 0
end = 5
while start < end:
    list1.append(int(random.randint(1,100)))
    start +=1

list2 = []
start = 0
end = 5
while start < end:
    list2.append(int(input("Please, enter five integers - ")))
    start +=1

list3 = [list1[i]*list2[i] for i in range(len(list1))]
# list3 = [i*j for i,j in zip(list1, list2)] - or
print(f"{list1=}")
print(f"{list2=}")
print(f"{list3=}")
