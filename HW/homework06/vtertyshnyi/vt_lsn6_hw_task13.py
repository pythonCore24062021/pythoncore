'''
13. Дві матриці заповнюються введенням з клавіатури. 
    В елементи третьої матриці такої ж розмірності записати більші з відповідних елементів перших двох. 
'''

from vt_helper import get_user_input_matrix
from vt_helper import print_matrix
from vt_helper import print_splitter

# set matrix size:
n = 2
m = 2

# set matrix values:
print("Enter the first matrix:")
matrix1 = get_user_input_matrix(n, m)
print_splitter()
print("Enter the second matrix:")
matrix2 = get_user_input_matrix(n, m)

# calculate 3rd matrix
matrix3 = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(
            max(
                matrix1[i][j], 
                matrix2[i][j]
            )
        )
    matrix3.append(row)

# display results
print_splitter()
print("You've entered - first matrix:")
print_matrix(matrix1)
print("You've entered - second matrix:")
print_matrix(matrix2)
print("We've calculated - third matrix:")
print_matrix(matrix3)
