

m = int(input("enter number of columns "))
n = int(input("enter number of rows "))
matrix1 = []
matrix2 = []
matrix3 = []

for i in range(m):
    b = []
    for j in range(n):
        b.append(int(input("enter matrix1 value ")))
    matrix1.append(b)


for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input("enter matrix2 value ")))
    matrix2.append(a)

print(" matrix1 ")
for i in range(m):
    for j in range(n):
        print( matrix1[i][j], end=" ")
    print()
print()

print(" matrix2 ")
for i in range(m):
    for j in range(n):
        print( matrix2[i][j], end=" ")
    print()
print()


for i in range(m):
    c = []
    for j in range(n):
        if matrix1[i][j] > matrix2[i][j]:
            c.append(matrix1[i][j])
        else:
            c.append(matrix2[i][j])
    matrix3.append(c)

print(" matrix3 ")
for i in range(m):
    for j in range(n):
        print(matrix3[i][j], end=" ")
    print()
