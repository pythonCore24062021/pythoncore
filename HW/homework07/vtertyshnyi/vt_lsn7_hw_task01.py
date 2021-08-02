'''
1. Написати функцію arithmetic, яка приймає 3 аргументи: 
    - перші 2 - числа, 
    - третій - операцію, яка повинна бути здійснена над ними. 
    Якщо третій аргумент
     +, додати їх; 
     якщо -, то відняти; 
     * - помножити; 
     / - розділити (перше на друге). 
    В інших випадках повернути рядок "Невідома операція".
'''

def arithmetic(a, b, op):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return 'First 2 parameters must be a number!'
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return f"Second parameter couldn't be 0 for the '{op}' operation!"
    else:
        return f"Unknown operation - '{op}'"

print(f"{arithmetic(0, 1, '+') = }")
print(f"{arithmetic(1, 2, '-') = }")
print(f"{arithmetic(2, 3, '*') = }")
print(f"{arithmetic(4, 5, '/') = }")
print(f"{arithmetic(1, 0, '!') = }")
print(f"{arithmetic('a', 0, '+') = }")
print(f"{arithmetic(0, 'b', '+') = }")
print(f"{arithmetic('a', 'b', '+') = }")
print(f"{arithmetic(0, 0, '!') = }")
print(f"{arithmetic(1, 0, '/') = }")