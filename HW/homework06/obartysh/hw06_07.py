import random

n = int(input("enter a number of elements in the list "))
random_list = [random.randint(-n, n) for i in range(n)]
answ = []
for i in random_list:
        if random_list.count(i) == 1: answ.append(i)
print(f'Random list: {random_list}')
print(f'unique values: {answ}')
