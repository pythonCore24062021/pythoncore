import copy
import random

# Task 1
'''. Заповнити один список випадковими числами, інший - введеними з клавіатури числами, в
третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.'''

"""
a_list = [i for i in range(10)]
print(a_list)
total = list()
b_list = list()
for i in range(10):
    b = int(input("Enter a value: "))
    b_list.append(b)
    print(b_list)
    total.append(a_list[i]+b_list[i])
print(f"Total list is {total}")
# --- подумати як зробити для списків різної довжини
"""

'''2. Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку.
Вивести на екран сам список, отримані суму і добуток його елементів.'''

"""
total = list()
dobutok = 1
i = input("Vvedit chyslo: ")
if i == 'stop':
    print("STOP THE LIST INCREASING")
while i != "stop":
    i = input("Vvedit chyslo: ")
    if i == 'stop':
        print("STOP THE LIST INCREASING")
        break
    else:
        total.append(int(i))
for i in total:
    dobutok = i*dobutok
print(f"The sum of list values is {sum(total)}. The 'Dobutok' is {dobutok}")
"""

"""
# Task 3
counter_1 = 0
counter_2 = 0
counter_3 = 0
l = list()
l = [random.randint(-5, 4) for i in range(20)]
for i in l:
    if i < 0:
        counter_1 = counter_1+1
    elif i > 0:
        counter_2 = counter_2+1
    else:
        counter_3 = counter_3+1
print(l)
print(f"The amount of values <0 is {counter_1}. The amount of values >0 is  {counter_2}. "
      f"The amount of values == 0 is {counter_3}")
"""

'''
# Task 4
dod_list = []
vid_list = []
l = [random.randint(-5, 5) for i in range(20)]
for i in l:
    if i > 0:
        dod_list.append(i)
    elif i < 0:
        vid_list.append(i)
print(f"Generated list is {l}.\nThe positive values of list are {dod_list}.\nThe negative values of list are {vid_list}")
'''

"""
# Task 5 -------- PLEASE COULD YOU EXPLAIN HOW IT WORKS ???
l = []
a = []
for i in range(20):
    r = random.randint(-100, 100)
    if r != 0:
        l.append(r)
print(f"The list is {l}")
a = copy.deepcopy(l)
for i in l:
    if i < 0:
        a.remove(i)
print(f"The list without values <0 {a}")
"""

# Task 6
'''
a = []
l = [random.randint(-100, 100) for i in range(20)]
print(l)
for i in l:
    if i % 2 == 0:
        a.append(l.index(i))
print(a)
'''
# Task 7
'''У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.'''
'''
l = [random.randint(1, 50) for i in range(20)]
# print(set(l))
print(l)
a = l[:]
for i in a:
    if a.index(i, 0, len(a)) == l.index(i, 1, len(l)+1):
        a.remove(i)
        print(a)
print(set(l))'''

# Task 8
"""
l = [random.randint(1, 50) for i in range(20)]
l.sort()
l[0], l[-1] = l[-1], l[0]
print(l)
"""

# Task 9
M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random.randint(1,10) * 11))
        print("%3d" % b[j], end=' ')
    a.append(b)
    print('   |', sum(b))

for i in range(M):
    print(" --", end=' ')
print()

for i in range(M):
    s = 0
    for j in range(N):
        s += a[j][i]
    print("%3d" % s, end=' ')
print()

# Task 10
'''
double = 0
matr = [[i for i in range(i, i+10)] for i in range(0,999,10)]
for i in matr:
    for j in i:
        if j >= 10 and j <= 99:
            double = double+1
print(matr)
print(f"The amount of double are {double}")
'''
# Task 11
"""
Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків). Програма повинна обчислювати суму 
введених елементів кожного рядка і записувати її в останній рядок. Наприкінці слід вивести отриману матрицю.

# Task 12
Знайти максимальний елемент серед мінімальних елементів стовпців матриці.

# Task 13
Дві матриці заповнюються введенням з клавіатури. В елементи третьої матриці такої ж розмірності записати більші з 
відповідних елементів перших двох.

# Task 14
У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.

# Task 15
Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням."""
'''
matr = list()
for i in range(5):
    row=[]
    for j in range(4):
        matr.append(j)
print(matr)

for i in matr:
    for j in i:
        if matr.index(j) == -1:
            j=random.randint(-100,100)
print(matr)
'''
