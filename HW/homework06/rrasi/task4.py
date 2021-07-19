#Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні.
#Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.

mylist = []
mylist_positive = []
my_list_negative = []
for i in range(-5,5):
    mylist.append(i)
    print(mylist)
for i in mylist:
    if (mylist[i] > 0) and (mylist[i] != 0):
        mylist_positive.append(mylist[i])
    if (mylist[i] < 0) and (mylist[i] != 0):
        my_list_negative.append(mylist[i])
print(mylist_positive, my_list_negative, mylist)