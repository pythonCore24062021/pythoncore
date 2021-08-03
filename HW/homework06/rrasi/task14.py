#У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.

import random

m = 10
n = 10
matrix = []

for i in range(m):
    b = []
    for j in range(n):
        b.append(int(random.randint(0, 100)))
    matrix.append(b)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j], matrix[i][len(matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]

print('Changed matrix:')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

