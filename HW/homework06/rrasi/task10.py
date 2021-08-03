#Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.
import random
n = 10
m = 6
counter = 0
matrix = [[j * i for j in range(m)] for i in range(n)]
print(matrix)
for i in range(n):
    matrix.append([random.randint(0, 999) for i in range(n)])
    for j in range(m):
        if matrix[i][j] // 100 == 0:
            counter += 1
        print(matrix[i][j], end=" ")
        print()
print(f'Count of 2digits numbers: {counter}')










import random

matrix = []
counter = 0
for i in range(5):
    matrix.append([random.randint(0, 999) for i in range(5)])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]//100 == 0:
            counter += 1
        print(matrix[i][j], end=" ")
    print()

print(f'Count of 2digits numbers: {counter}')