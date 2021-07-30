import random

matrix = []
matrix2 = []
for i in range(3):
    matrix.append([random.randint(0, 10) for i in range(3)])


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


print('Original matrix:')
print_matrix(matrix)

index_list = sorted(range(len(matrix)), key=lambda i: matrix[0][i])

for i in range(len(matrix)):
    line = []
    for j in range(len(matrix[0])):
        line.append(matrix[i][index_list[j]])
    matrix2.append(line)

print('Changed matrix:')
print_matrix(matrix2)
