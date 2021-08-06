import random

my_list = [random.randint(-50,50) for item in range(30)]
print(my_list)
even_index = my_list[::2]
print(str(even_index))