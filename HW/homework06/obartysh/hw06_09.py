import random

m = int(input("enter number of columns "))
n = int(input("enter number of rows "))
a = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(random.randint(-1000, 1000) * (m+1))
        print("%3d" % b[j], end=' ')
    a.append(b)
    print('   |', sum(b))

for i in range(n):
    print(" --", end=' ')
print()

for i in range(n):
    s = 0
    for j in range(m):
        s += a[j][i]
    print("%3d" % s, end=' ')
print()
