'''
9. Порахувати суми кожного рядка і кожного стовпця матриці. 
   Доповнити її 
    - стовпцем, який містить суми елементів рядків 
    - та рядком, елементами якого є суми елементів стовпців.
'''

import vt_helper

# create initial matrix
matrix = vt_helper.get_matrix()
vt_helper.print_matrix(matrix)

# add a column with row sum
for row in matrix:
    row.append(sum(row))

# initialize a row with a columns sum
total = []
for i in matrix[0]:
    total.append(0)

# calculate row with a columns sum
for row in matrix:
    for i in range(len(row)):
        total[i] += row[i]

# add a row with a columns sum to initial matrix
matrix.append(total)

# display results:
vt_helper.print_splitter()
vt_helper.print_matrix(matrix)
