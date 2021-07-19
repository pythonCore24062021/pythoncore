#Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні.
#Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
count_positive= 0
count_negative = 0
count_null = 0

mylist = []
for i in range(-5,5):
    mylist.append(i)
    print(mylist)
for x in mylist:
    if x > 0:
        count_positive +=1
    if x < 0:
        count_negative +=1
    if x == 0:
        count_null += 1
print(count_positive, count_negative, count_null)