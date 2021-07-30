import random

n = int(input("enter a number of elements in the list "))
random_list = [random.randint(-5, 5) for i in range(n)]

positive_list = []
negative_list = []

for i in range(len(random_list)):
    if random_list[i] > 0:
        positive_list.append(random_list[i])
    elif random_list[i] < 0:
        negative_list.append(random_list[i])

print(f'Random list: {random_list}')
print(f'list of positive elements: {positive_list}')
print(f'negative of negative elements: {negative_list}')

