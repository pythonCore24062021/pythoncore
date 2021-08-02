'''
4. Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів. 
Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.
'''

n = 5
m = 10
line = '#'
fill_in = ' '

for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1:
            print(line, end='')
            continue
        if i < n - 1:
            print(line, end='') if j == 0 or j == m - 1 else print(fill_in, end='')
            continue
    print()
