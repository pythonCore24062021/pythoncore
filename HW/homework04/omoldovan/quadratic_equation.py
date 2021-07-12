# ax^2 + bx + c == 0, a!=0
import math

a = int(input("Enter a first (a) value of the equation: "))
while a == 0:
    print("This is a linear equation. Enter a new value not equal to 0!!!")
    a = int(input("Enter a first (a) value of the equation: "))
else:
    b = int(input("Enter a second (b) value of the equation: "))
    c = int(input("Enter a third (c) value of the equation: "))
# Розв'язування неповних квадратних рівнянь
'''if b == 0 and c == 0:
    print("x = 0")
    quit()
if c == 0:
    x1 = 0
    x2 = -b/a   ---- this cases are covered in the discriminant section'''
if b == 0 and -c/a < 0:
    print("Немає дійсних коренів")
    quit()
# Зведеня квадратного рівняння
'''if a%2 == 0 and b%2 == 0 and c%2 == 0:
    a = a/2
    b = b/2
    c = c/2
elif a%3 == 0 and b%3 == 0 and c%3 == 0:
    a = a / 3
    c = c / 3
    b = b / 3
elif a%5 == 0 and b%5 == 0 and c%5 == 0:
    a = a / 5
    b = b / 5
    c = c / 5
elif a%7 == 0 and b%7 == 0 and c%7 == 0:
    a = a / 7
    b = b / 7
    c = c / 7'''

if a%a == 0 and b%a == 0 and c%a == 0:
    a_new = a/a
    b_new = b/a
    c_new = c/a

print(f"The equation is {a_new}x^2 + {b_new}x + {c_new} = 0")


# Розв'язування повних квадратних рівнянь через дискримінант

Diskriminans = b_new**2-(4*a_new*c_new)
if Diskriminans < 0:
    print("Рівняння розв'язків немає")
else:
    print(f"Diskriminans is equal to {Diskriminans}")
    x1 = (-b_new + math.sqrt(Diskriminans))/2*a_new
    x2 = (-b_new - math.sqrt(Diskriminans))/2*a_new


print(f"The x1 = {x1}")
print(f"The x2 = {x2}")

