# Task12
import random

N=7
M=5
A=[]
B=[]
for i in range(N):
    A.append([])
    for j in range(M):
        A[i].append(random.randint(0,999))

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=" | ")
    print()

for j in range(M):
    mn = A[i][j]
    for i in range(N):
        if A[i][j] < mn:
            mn = A[i][j]
    B.append(mn)
    print(mn, end=' * ')
print()

print(f"The value we are looking for is {max(B)}")

