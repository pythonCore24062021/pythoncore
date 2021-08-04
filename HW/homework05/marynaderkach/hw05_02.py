counter = 0
for i in range(10):
    num = int(input('Enter a number: '))
    if num < 2:
        print("Enter number greater then 2")
        num = int(input('Enter a number: '))
    if num % 5 == 0:
        counter += 1

print(f"You entered {counter} multiples of 5")
