number = '4311'
res = 0
number_l = list(number)
number_int = int(number)
for i in number_l:
    res = res + int(i)*(int(i)+1)

print(number_l)
print(number_l.reverse())
print(number_l.sort())
