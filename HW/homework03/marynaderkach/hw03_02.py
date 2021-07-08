number = 2143

mult = 1
for i in str(number):
    mult = mult * int(i)

print(f"Multiplication of digits in the {number}: {mult}")
print(f"Reverse {number}: {str(number)[::-1]}")
print(f"Sorting {number}: {''.join(sorted(str(number)))}")
