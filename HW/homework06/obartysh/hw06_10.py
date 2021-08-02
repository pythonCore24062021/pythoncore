import random

m = int(input("enter number of columns "))
n = int(input("enter number of rows "))
counter = 0
matrix = []

for i in range(m):
    b = []
    for j in range(n):
        b.append(int(random.randint(0, 999)))
    matrix.append(b)

for i in range(m):
    for j in range(n):
        if matrix[i][j] // 100 == 0:
            counter += 1

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
print(f'Count of 2digits numbers: {counter}')

