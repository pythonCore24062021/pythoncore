import random

my_list = [random.randint(-50,50) for item in range(30)]
print(my_list)
unique_list  = sorted(set(my_list))
print(unique_list)

maxi = max(unique_list)
mini = min(unique_list)
print(f"max value: {maxi}")
print(f"min value: {mini}")

unique_list = [mini if i == maxi else maxi if i == mini else i for i in unique_list]
print(unique_list)