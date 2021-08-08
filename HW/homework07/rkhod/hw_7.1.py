# Task 1
import random


def arithmetic(num1, num2, arg):
    if arg == "+":
        print(num1 + num2)
    elif arg == "-":
        print(num1 - num2)
    elif arg == "*":
        print(num1 * num2)
    elif arg == "/":
        print(num1 / num2)
    else:
        print(f"{arg} - unknown operation ")


arithmetic(random.randint(1, 99), random.randint(1, 99), "*")
