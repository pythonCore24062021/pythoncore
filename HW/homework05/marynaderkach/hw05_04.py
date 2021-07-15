n = int(input('Enter a height: '))
m = int(input('Enter a width: '))
outline = '-'
fill = '+'

for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1:
            print(outline, end='')
            continue
        if i < n - 1:
            if j == 0 or j == m - 1:
                print(outline, end='')
            else:
                print(fill, end='')
            continue
    print()
