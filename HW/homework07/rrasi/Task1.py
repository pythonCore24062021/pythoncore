#1. Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена
#над ними. Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге).
#В інших випадках повернути рядок "Невідома операція".
def arithmetic(arg1, arg2, operation):
    if operation == '+':
        return arg1 + arg2
    elif operation == '-':
        return arg1 - arg2
    elif operation == '*':
        return arg1 * arg2
    elif operation == '/':
        return arg1 / arg2
    else:
        return "Unknown operation"

a = float(input("value a = "))
b = float(input("value b = "))
c = input("operation ")
print(arithmetic(a, b, c))
