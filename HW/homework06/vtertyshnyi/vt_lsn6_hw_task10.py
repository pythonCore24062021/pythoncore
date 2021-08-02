'''
10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран. 
    Порахувати кількість двозначних чисел в ній.
'''

from typing import ItemsView

# determine is the number has 2 digits
def is_NN(num):
    count = 0
    while num:    
        num = int(num/10)
        count += 1
    return True if count == 2 else False

# create initial matrix
matrix = [
    item
    for item in range(1000)
]

# separate numbers consists from 2 digits
matrix_NN = [
    item
    for item in matrix
    if is_NN(item)
]

# display results
print(f"{matrix = }")
print(f"{matrix_NN = }")
print(f"{len(matrix_NN) = }")