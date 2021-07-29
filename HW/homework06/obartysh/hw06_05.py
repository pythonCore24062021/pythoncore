import random

n = int(input("enter a number of elements in the list "))
random_list = [random.randint(-n, n) for i in range(n)]

positive_list = []

for i in range(len(random_list)):
    if random_list[i] > 0:
        positive_list.append(random_list[i])

print(f'Random list: {random_list}')
print(f'list of positive elements: {positive_list}')
