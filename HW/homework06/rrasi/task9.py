#Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем,
# який містить суми елементів рядків та рядком, елементами якого є суми елементів стовпців.

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
for i in range(3):
    for j in range(3):
        print(M[i][j], end="\t")
    print()
print()
for i in range(3):
    M[i].append(sum(M[i]))
for i in range(3):
    for j in range(3+1):
        print(M[i][j], end="\t")
    print()
print()
row = []
for i in range(3):
    sum = 0
    for j in range(3):
        sum += M[j][i]
    row.append(sum)
M.append(row)
for i in range(3+1):
    for j in range(3+1):
        if not (i == 3) and not (j == 3):
            print(M[i][j], end="\t")
    print()
print()


