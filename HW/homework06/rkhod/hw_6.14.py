# Task 14
import random

N=10
M=10
A=[]
for i in range(N):
    A.append([])
    for j in range(M):
        A[i].append(random.randint(0, 99))

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end="| ")
    print()
print()
