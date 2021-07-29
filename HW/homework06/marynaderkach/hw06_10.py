import random

matrix = []
counter = 0
for i in range(10):
    matrix.append([random.randint(0, 999) for i in range(10)])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]//100 == 0:
            counter += 1
        print(matrix[i][j], end=" ")
    print()

print(f'Count of 2digits numbers: {counter}')
