import random
my_list = []
positivelist = []
negativelist = []

for i in range(0,20):
    n = random.randint(-5,5)
    my_list.append(n)
    my_list.sort()
print(f"Randomly generated list: {my_list}")

for item in my_list:
    if item >= 0:
        positivelist.append(item)
    if item < 0:
         negativelist.append(item)

print("positive list ", positivelist)
print(f"negative list before delete {negativelist}")
negativelist.clear()
print(f"Negative list after: {negativelist}")
print(f"List with positive numbers only: {positivelist}")