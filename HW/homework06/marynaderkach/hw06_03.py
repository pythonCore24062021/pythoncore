import random

random_list = [random.randint(-5, 4) for i in range(20)]

sum_plus = 0
sum_minus = 0
zeros = 0

for i in range(len(random_list)):
    if random_list[i] > 0:
        sum_plus += 1
    elif random_list[i] < 0:
        sum_minus += 1
    else:
        zeros += 1

print(f'Random list: {random_list}')
print(f'Positive values: {sum_plus}')
print(f'Negative values: {sum_minus}')
print(f'Zero values: {zeros}')
