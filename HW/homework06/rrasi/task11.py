#Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків). Програма повинна обчислювати суму введених
#елементів кожного рядка і записувати її в останній рядок. Наприкінці слід вивести отриману матрицю.

m = 5
n = 4
matrix = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)
additional_line = []
for i in range(len(matrix)):
    additional_line.append(sum(matrix[i]))
matrix.append(additional_line)
# For printing the matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()









