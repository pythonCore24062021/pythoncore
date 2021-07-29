import random
print("Guess the number from less than 10 attemps")
a= random.randint(0,100)
numberOfAttemps=0
b=int(input())
while numberOfAttemps <10:
    print(f" Your guess = {b}", end='')
    numberOfAttemps +=1
    if(a>b):
        print(f" Too less \t You used {numberOfAttemps} all your attemps, this number {b} is not correct")
    if ( a<b):
        print(f" Too much \t You used {numberOfAttemps} all your attemps, this number {b} is not correct")
    if (a==b): break
    b = int(input())
