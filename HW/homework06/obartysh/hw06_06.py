import random

n = int(input("enter a number of elements in the list "))
random_list = [random.randint(-n, n) for i in range(n)]

binate_index_values = []

binate_index_values = [i for i in range(len(random_list)) if random_list[i] % 2 == 0]

print(f'Random list: {random_list}')
print(f'list of binate indexes: {binate_index_values}')
