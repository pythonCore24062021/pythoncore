a = float(input('Enter a: '))
b = float(input('Enter b: '))

sum = a + b
sub = a - b
mult = a * b
div = 0 if b == 0 else a / b

print('The sum of {0} and {1} is {2}'.format(a, b, sum))
print('The subtract of {0} and {1} is {2}'.format(a, b, sub))
print('The multiplication of {0} and {1} is {2}'.format(a, b, mult))
print('The division of {0} and {1} is {2}'.format(a, b, div))
