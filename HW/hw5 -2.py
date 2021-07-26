
i = 0
count = 0
while not i == 10:
    n = int(input(f"Enter the {i+1} number: "))
    if n > 2:
        i += 1
        if n % 5 == 0:
            count += 1
print(f'There are {count} numbers that are divisible by 5')
