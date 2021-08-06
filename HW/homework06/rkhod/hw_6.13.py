# Task 13
import random

N=3
M=3
A=[]
for i in range(N):
    A.append([])
    for j in range(M):
        A[i].append(int(input("Please, specify the matrix 1 value...")))

B=[]
for i in range(N):
    B.append([])
    for j in range(M):
        B[i].append(int(input("Please, specify the matrix 2 value...")))

print(A)
print(B)

C=[]
for i in range(N):
    C.append([])
    for j in range(M):
        if A[i][j] >= B[i][j]:
            C[i].append(A[i][j])
        else:
            C[i].append(B[i][j])

print(f"The matrix we are looking for is")
for i in range(len(C)):
    for j in range(len(C[i])):
        print(C[i][j], end=" | ")
    print()
