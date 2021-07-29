import random

random_list = [random.randint(-5, 5) for i in range(20)]

list_plus = []
list_minus = []

for i in range(len(random_list)):
    if random_list[i] > 0:
        list_plus.append(random_list[i])
    elif random_list[i] < 0:
        list_minus.append(random_list[i])

print(f'Random list: {random_list}')
print(f'Positive values: {list_plus}')
print(f'Negative values: {list_minus}')
