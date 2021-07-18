#1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами,
#в третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.

#import random
#a = random.randint(0, 100)
#i = 0
#while i < 5:
#    i += 1
#    a = random.randint(0, 100)
#    print(a)
#
#randomlist = [a]
#randomlist.append(a)
#print(randomlist)

import random
randomlist = random.sample(range(10, 30), 5)
print(randomlist)


#import random
#randomlist = []
#for i in range(0,5):
#n = random.randint(1,30)
#randomlist.append(n)
#print(randomlist)

input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
print('list: ', user_list)
three = map(sum, zip(randomlist, user_list))
print(three)


a = [1,2,3,4,5]
b = [6,7,8,9,10]
zip(a, b)
map(lambda x: x[0] + x[1], zip(a, b))

three = [sum(i) for i in zip(a,b)]