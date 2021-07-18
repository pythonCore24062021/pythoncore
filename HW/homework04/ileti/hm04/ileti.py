import math

a= int(input("value for a: "))
b= int(input("value for b: "))
c= int(input("value for c: "))

d = b**2 - 4*a*c
print(d)
if d < 0:
    print("solution1 value is less than 0")
elif d == 0:
    x = -b/2*a
    print(" solution2 x=" + str(x))
else:
    x1 = (-b+math.sqrt((b**2)-(4*a*c)))/2*a
    x2 = (-b-math.sqrt((b**2)-(4*a*c)))/2*a
    print(f"solution3 x1 = {x1}, x2 = {x2}")