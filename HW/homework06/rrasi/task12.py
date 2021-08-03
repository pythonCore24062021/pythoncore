#Знайти максимальний елемент серед мінімальних елементів стовпців матриці.

import random

m = 5
n = 4
matrix = []

for i in range(m):
    b = []
    for j in range(n):
        b.append(int(random.randint(0, 100)))
    matrix.append(b)

min_line = []
min_line = [min(j) for j in zip (*matrix)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

print(f'minimum elements in columns {min_line}')
print(f'maximum value of minimum elements {max(min_line)}')
