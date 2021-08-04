import random

n = int(input("enter a number of elements in the list "))
random_list = [random.randint(-n, n) for i in range(n)]
print(f'Random list: {random_list}')

min = random_list.index(min(random_list))
max = random_list.index(max(random_list))

random_list[max], random_list[min] = random_list[min], random_list[max]
print(f'Random list: {random_list}')
