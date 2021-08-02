# Task11

N=5
M=4
A=[]
for i in range(N):
    A.append([])
    for j in range(M):
        A[i].append(int(input("Please, specify the matrix value...")))

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end='  ')
    print("| ", sum(A[i]))
    print()
