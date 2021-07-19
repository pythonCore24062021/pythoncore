#Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран.
#Видалити з списку всі від’ємні елементи і знову вивести.
mylist = []
mylist_positive = []
x = 0
for i in range(-5,10):
    mylist.append(i)
    print(mylist)
    for x in range(len(mylist)):
        if x < len(mylist) and mylist[x] < 0:
            mylist.remove(mylist[x])
    print(mylist)

mylist = []
mylist_positive = []
x = 0
for i in range(-5,10):
    mylist.append(i)
    print(mylist)
while x < len(mylist):
    if mylist[x] < 0:
        mylist.remove(mylist[x])
        continue
    x += 1
    print(mylist)
