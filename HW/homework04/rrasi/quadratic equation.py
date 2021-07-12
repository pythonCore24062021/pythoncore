print('The equation a•x²+b•x+c=0')
a = input('Enter value a: ')
b = input('Enter value b: ')
c = input('Enter value c: ')
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
print('discriminant = ' + str(discriminant))
if discriminant < 0:
    print('No roots')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))