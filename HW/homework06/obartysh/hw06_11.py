matrix = []

for i in range(4):
    b = []
    for j in range(5):
        b.append(int(input()))
    matrix.append(b)

extra_line = []
for i in range(len(matrix)):
    extra_line.append(sum(matrix[i]))
matrix.append(extra_line)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
