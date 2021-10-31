
import math
def square(a):
    p = a * 4
    s = a ** 2
    d = a * math.sqrt(2)
    return p, s, d
n = int(input("square length "))
print(n)
print(square(n))