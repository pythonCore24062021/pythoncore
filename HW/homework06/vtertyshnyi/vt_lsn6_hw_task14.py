'''
14. У матриці 10x10 поміняти значення елементів у кожному рядку, 
    розташовані відповідно на головній та бічній діагоналях.
'''

from vt_helper import get_matrix
from vt_helper import print_matrix
from vt_helper import print_splitter

# set matrix
n = 10

matrix = get_matrix(n, n)
print_matrix(matrix)

# swap elements
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][i], matrix[i][n-i-1] = matrix[i][n-i-1], matrix[i][i]

print_splitter()
print_matrix(matrix)
