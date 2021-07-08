number = input("Enter a number (no more than 4 symbols allowed): ")
number_l = list(number)
# Revers numbers
reversed_number = number[::-1]
print(reversed_number)

# Sort numbers
print(sorted(number_l))

# Result of multiplication of all symbols one by one

dobutok = int(number[0]) * int(number[1:2]) * int(number[2:3]) * int(number[3:4])
print(dobutok)
