# Task10
import random

N=7
M=5
A=[]
count = 0
for i in range(N):
    A.append([])
    for j in range(M):
        A[i].append(random.randint(0,999))

for i in range(len(A)):
    for j in range(len(A[i])):
        if 9 < A[i][j] < 100:
            count +=1
        print(A[i][j], end='  ')
    print()

print(f"The amount of two-digit numbers is = {count}")