def get_known_values (param):
    while True:
        try: 
            print(f"Enter '{param}': ")
            n = float(input())
            break
        except ValueError:
            print(f"'{param}' must be a number. Please, try one more time!")
    return n

print ("The known 'a', 'b', and 'c' numbers of the quadratic equation required: \
    \n\ta*x^2 + b*x + c = 0;")

a = get_known_values('a')
b = get_known_values('b')   
c = get_known_values('c')

print("Results:")

if a == b == c == 0:
    print("Nothing to resolve!")
elif a == 0:
    print ("It's not a quadratic equation!")
elif b == c == 0:
    print ("x1 = x2 = 0")
else:
    D = b**2 - 4 * a * c
    #print (f"D = {D}")
    
    if D < 0:
        print("No decisions")
    elif D == 0:
        x = -b / (2 * a)
        print(f"x1 = x2 = {x}")
    else:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        print(f"x1 = {x1}\nx2 = {x2}")
