def arithmetic(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return 0 if b == 0 else a / b
    else:
        return "Unknown operation"


print(arithmetic(1, 2, "/"))
