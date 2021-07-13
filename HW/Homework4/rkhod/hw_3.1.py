import math

# Set the values for quadratic equation
print("Example for 'ax^2 + bx + c = 0'")
print("Enter a value for:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Print the discriminant
discr = (b**2) - (4*a*c)
print(f"Discriminant D = {discr}")

# Solution
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("No root")
