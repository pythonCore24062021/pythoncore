import random

matrix = []
for i in range(5):
    matrix.append([random.randint(0, 5) for i in range(5)])

extra_line = []
for i in range(len(matrix)):
    matrix[i].append(sum(matrix[i]))

for i in range(len(matrix[0])):
    total_column = 0
    for j in range(len(matrix)):
        total_column += matrix[j][i]
    extra_line.append(total_column)
matrix.append(extra_line)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
