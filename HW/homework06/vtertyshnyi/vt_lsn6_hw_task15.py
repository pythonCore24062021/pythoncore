'''
15. Змінити послідовність стовпців матриці так, 
    щоб елементи її першого рядка були відсортовані за зростанням.
'''

from vt_helper import get_matrix
from vt_helper import print_matrix
from vt_helper import print_splitter

# set matrix
n = 2
m = 3
matrix = get_matrix(n, m)

# get sorted items indexes
sorted_items_indexes = [
    sorted(matrix[0]).index(item)
    for index, item in enumerate(matrix[0])
]

# display initial state
print("Intial matrix:")
print_matrix(matrix)

# swap columns
matrix_swap_columns = []
for row in matrix:
    new_row = []
    for i in range(len(row)):
        index = sorted_items_indexes.index(i)
        new_row.append(row[index])
    matrix_swap_columns.append(new_row)
matrix = matrix_swap_columns.copy()

# display results
print_splitter()
print("Result matrix:")
print_matrix(matrix)
