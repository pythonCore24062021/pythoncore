import random

random_list = random.sample(range(-100, 100), 20)
print(f'Random list: {random_list}')

random_list = [i for i in random_list if i > 0]
print(f'Random list: {random_list}')