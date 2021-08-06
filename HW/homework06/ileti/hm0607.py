import random
unique_list  = []
my_list = [random.randint(-50,50) for item in range(30)]
print(my_list)
# unique_list  = sorted(set(my_list))
# print(unique_list)

for i in my_list:
    if my_list.count(i) == 1: unique_list.append(i)
print(unique_list)