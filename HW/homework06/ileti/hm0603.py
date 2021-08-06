import random
my_list = []
for i in range(0,20):
    n = random.randint(-5,4)
    my_list.append(n)
    my_list.sort()
print(my_list)
pos_count = 0
neg_count = 0
zero_count = 0

for num in my_list:
    if num > 0:
        pos_count +=1
    if num < 0:
        neg_count +=1
    if num == 0:
        zero_count +=1
print(f"Positive are: {pos_count}")
print(f"Negative are: {neg_count}")
print(f"Zero are: {zero_count}")