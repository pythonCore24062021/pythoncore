import random
my_list = []
positivelist = []
negativelist = []

for i in range(0,20):
    n = random.randint(-5,5)
    my_list.append(n)
    my_list.sort()
print(my_list)

for item in my_list:
    if item > 0:
        positivelist.append(item)
    if item < 0:
         negativelist.append(item)
    if item  ==0:
        continue
print(f"Positive list count: {len(positivelist)}")
print("positive list ", positivelist)
print(f"Negative list count: {len(negativelist)}")
print("negative list", negativelist)
