count = 0
for i in range(9):
    n = int(input("enter integer value "))
    if n <= 2:
        print("enter number that is greater 2")
        n = int(input("enter integer value "))
    else:
        if n % 5 == 0:
            count += 1

print(f"There are {count} numbers that multiples 5 ")
