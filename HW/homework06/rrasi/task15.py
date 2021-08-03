#Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.

import random

m = 10
n = 10
matrix = []
matrix2 = []

for i in range(m):
    b = []
    for j in range(n):
        b.append(int(random.randint(0, 100)))
    matrix.append(b)
sorted_list = sorted(range(len(matrix)), key=lambda i: matrix[0][i])

for i in range(len(matrix)):
    line = []
    for j in range(len(matrix[0])):
        line.append(matrix[i][sorted_list[j]])
    matrix2.append(line)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
print("New matrix")
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        print(matrix2[i][j], end=" ")
    print()



