'''
12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.
'''

from vt_helper import get_matrix
from vt_helper import print_matrix
from vt_helper import print_splitter

matrix = get_matrix(5, 5)

# find minimals in each column
min_in_column = []
for i in range(len(matrix[0])):
    column = []
    for j in range(len(matrix)):
        column.append(matrix[j][i])
    min_in_column.append(min(column))

# display results:
print_matrix(matrix)
print(f"Max element from column minimals: {max(min_in_column)}")
