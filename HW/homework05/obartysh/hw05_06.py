p = float(input('Enter p: '))
h = float(input('Enter h: '))
number = float(input('Enter a number: '))
suma = 0
mult = 1
listofnumbers = []

while number != p and number != h:
    if number < p:
        suma += number
    if number > h:
        mult *= number
    if p < number < h:
        listofnumbers.append(number)
    number = float(input('Enter a number: '))

print(f"Suma is {suma}")
print(f'Multiplication is {mult}')
print(f"List of number between p and h:{listofnumbers}")
