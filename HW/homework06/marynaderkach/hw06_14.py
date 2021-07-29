import random

matrix = []
for i in range(10):
    matrix.append([random.randint(0, 10) for i in range(10)])


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


print('Original matrix:')
print_matrix(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j], matrix[i][len(matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]

print()
print('Changed matrix:')
print_matrix(matrix)
