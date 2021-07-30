import random

random_list = [random.randint(-5, 4) for i in range(20)]

sum_plus = 0
sum_minus = 0
zero = 0

for i in range(len(random_list)):
    if random_list[i] == 0:
        zero += 1
    elif random_list[i] < 0:
        sum_minus += 1
    else:
        sum_plus += 1

print(f'Random list: {random_list}')
print(f'number of zero in the list: {zero}')
print(f'number of negative elements: {sum_minus}')
print(f'number of positive elements: {sum_plus}')
