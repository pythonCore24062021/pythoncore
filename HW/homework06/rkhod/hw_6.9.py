# Task 9

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end='  ')
    print(sum(A[i]))
    print()

for i in range(len(A)):
    s = 0
    for j in range(len(A)):
        s += A[j][i]
    print(s, end=' ')
print()
