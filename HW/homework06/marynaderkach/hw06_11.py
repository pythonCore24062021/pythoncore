rows = 5
columns = 4
matrix = []

print(f'Enter the {rows} x {columns} matrix: ')
for i in range(rows):
    matrix.append(list(map(int, input().rstrip().split()))[:4])

extra_line = []
for i in range(len(matrix)):
    extra_line.append(sum(matrix[i]))
matrix.append(extra_line)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
