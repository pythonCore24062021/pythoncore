def arithmetic(arg1, arg2, op):
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2
    else:
        return "Unknown operation"

a = float(input("enter first number a = "))
b = float(input("enter first number b = "))
c = input("enter operation ")
print(arithmetic(a, b, c))