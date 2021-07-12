import math

a = int(input('Enter coeffs of a: '))
b = int(input('Enter coeffs of b: '))
c = int(input('Enter coeffs of c: '))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print('This equation has no solution')
elif discriminant == 0:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(f'This equation has one solution: {x1:.4f}')
else:
    x1 = (-b + math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
    x2 = (-b - math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
    print(f'This equation has two solutions: {x1:.4f} or {x2:.4f}')
