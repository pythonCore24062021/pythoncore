print('ax**2+bx+c=0')
a = int(input('Enter the first number (not 0): '))

b = int(input('Enter the second number (not 0): '))

c = int(input('Enter the third number and press <Enter>: '))

d = b ** 2 - 4 * a * c

if (d>0):
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x1 =  ', int(x1))
    print('x2 =  ', int(x2))
elif (d == 0):
    print('x =  ', -b / ( 2 * a ))
else:
    print("The equation has no solution")