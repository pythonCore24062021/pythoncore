import random

random_list = [random.randint(-100, 100) for i in range(20)]
print(f'Random list: {random_list}')

even_indexes = [i for i in range(len(random_list)) if random_list[i] % 2 == 0]
print(f'Even indexes: {even_indexes}')
