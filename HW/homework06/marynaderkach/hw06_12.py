import random

matrix = []
for i in range(4):
    matrix.append([random.randint(0, 5) for i in range(5)])

min_line = []
result = [min(i) for i in zip(*matrix)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
print(result)
