# Task5
p = 10
h = 25
int1 = int(input('Please specify any number - '))
a = 0
b = 1
c = 0
while int1 != p and int1 != h:
    if p < int1 < h:
        c += 1
    if int1 < p:
        a += int1
    if int1 > h:
        b *= int1
    # if p < int1 > h:
    #     c += 1
    int1 = int(input('Please specify any number - '))
else:
    print("Bingo")
    print(f"P = {p} \nH = {h} \n* Summ of int < p = {a} \n"
          f"* Multiple of int < h = {b} \n* Number of int between p and h = {c}")
