print("введіть кофіцієнти для квадратного рівняння")
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
print("ax^2 + bx + c = 0:")
discr = b ** 2 - 4 * a * c
print("Дискримінант D = ",  discr)

if discr > 0:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif discr == 0:
    x = -b / (2 * a)
    print("x = ",  x)
else:
    print("немає дійсних коренів")
