i = 0
count = 0
while i < 3:
    n = int(input("Set the number': "))
    i += 1
    if n % 5 == 0:
       count += 1
print(count)


i = 0
count = 0
while not i == 10:
    n = int(input(f"Set the {i+1} number': "))
    if n > 2:
        i += 1
        if n % 5 == 0:
            count += 1
print(count)
