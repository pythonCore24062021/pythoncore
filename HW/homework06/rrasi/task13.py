#Дві матриці заповнюються введенням з клавіатури. В елементи третьої матриці такої ж р
#озмірності записати більші з відповідних елементів перших двох.

m = 3
n = 2
matrix1 = []
matrix2 = []
matrix3 = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix1.append(a)
for i in range(m):
    b = []
    for j in range(n):
        b.append(int(input()))
    matrix2.append(b)

# For printing the matrix
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        print(matrix1[i][j], end=' ')
    print()
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        print(matrix2[i][j], end=' ')
    print()
for i in range(len(matrix1)):
    matrix3.append([max(k) for k in zip(matrix1[i], matrix2[i])])
    for j in range(len(matrix1[i])):
        print(matrix3[i][j], end=' ')
    print()