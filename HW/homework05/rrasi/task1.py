import random

a = random.randint(0, 100)
print(a)
i = 0
while i < 10:
    n = int(input("Set the number': "))
    if n > a:
        print('Your number', n, ' is larger then Random A')
        i += 1
        print('Turn number', i)
    elif n < a:
        print('Your number', n, ' is less then Random A')
        i += 1
        print('Turn number', i)
    elif n == a:
        print('Your number', n, ' is correct')
        i += 1
        print('Turn number', i)
        break
else:
    print('The last Turn number', i)
    print('Correct number is', a)
    print('Game Over!')



