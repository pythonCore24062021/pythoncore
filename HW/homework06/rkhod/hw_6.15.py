# Task 15
import random


N = 3
M = 5
A = []
for i in range(N):
    A.append([])
    for j in range(M):
        A[i].append(random.randint(0, 99))

for i in range(len(A)):
    for j in range(len(A[i])):
        print((A[i][j]), end="| ")
    print()
print("_")

sortedList = sorted(range(len(A)), key=lambda i: A[0][i])
B=[]
for i in range(len(A)):
    C = []
    for j in range(len(A[0])):
        C.append(A[i][sortedList[j]])
    B.append(C)

for i in range(len(B)):
    for j in range(len(B[i])):
        print((B[i][j]), end="| ")
    print()

