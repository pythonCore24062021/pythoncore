import random
a = []
for i in range(0,999):
    n = random.random()
    n = n*20
    n=int(n)
    n = n-10
    a.append(n)
print(a)
neg = []
pos = []
for i in a:
    if i <0:
        neg.append(i)
    if i >0:
        pos.append(i)
    elif i ==0:
        break
print(neg)
print(pos)

