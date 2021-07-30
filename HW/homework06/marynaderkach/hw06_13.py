rows = 2
columns = 2
matrix = []
matrix2 = []
matrix3 = []


def fill_matrix(m):
    print(f'Enter the {rows} x {columns} matrix: ')
    for i in range(rows):
        m.append(list(map(int, input().rstrip().split()))[:2])


fill_matrix(matrix)
fill_matrix(matrix2)

for i in range(len(matrix)):
    matrix3.append([max(k) for k in zip(matrix[i], matrix2[i])])
    for j in range(len(matrix[i])):
        print(matrix3[i][j], end=' ')
    print()
