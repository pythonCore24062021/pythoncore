i = 0
while i < 3:
    n = int(input("Set the number': "))
    i += 1
count = 0
while n > 0:
    n, digit = divmod(n, 10)
    for n in range(digit):
     if digit % 5 == 0:
        count +=1
print(count)



