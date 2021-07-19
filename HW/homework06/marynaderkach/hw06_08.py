import random

random_list = [random.randint(-5, 5) for i in range(5)]
print(f'Random list: {random_list}')

index_min = random_list.index(min(random_list))
index_max = random_list.index(max(random_list))

random_list[index_max], random_list[index_min] = random_list[index_min], random_list[index_max]
print(f'Random list: {random_list}')