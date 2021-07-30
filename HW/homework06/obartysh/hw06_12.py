import random

m = int(input("enter number of columns "))
n = int(input("enter number of rows "))
matrix = []

for i in range(m):
    b = []
    for j in range(n):
        b.append(int(random.randint(-1000, 1000)))
    matrix.append(b)

min_line = []
min_line = [min(j) for j in zip(*matrix)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

print(f'print list of minimum elements in columns {min_line}')
print(f'print maximum value of the list of minimum elements in columns {max(min_line)}')

