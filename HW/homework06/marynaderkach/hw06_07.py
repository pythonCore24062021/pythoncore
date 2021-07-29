import random

random_list = [random.randint(-5, 5) for i in range(20)]
print(f'Random list: {random_list}')
print(f'Unique values: {list(set(random_list))}')
