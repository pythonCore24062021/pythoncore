import random

random_list = random.sample(range(10, 30), 5)

entered_list = []
for i in range(0, 5):
    entered_list.append(int(input('Enter number: ')))

sum_list = []
for i in range(0, 5):
    sum_list.append(random_list[i] + entered_list[i])

print(f'Random list: {random_list}')
print(f'Random list: {entered_list}')
print(f'Sum of 1st and 2nd lists: {sum_list}')
