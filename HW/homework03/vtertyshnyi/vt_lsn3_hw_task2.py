row_splitter = '\n' + '#' * 100 + '\n'

num = 2534

print(row_splitter)
sum_of_digits = 0
for i in str(num):
    sum_of_digits += int(i)
print(f"PART 1 = > Sum of digits in the {num} number is equal to {sum_of_digits}")
print(row_splitter)

print(row_splitter)
print(f"PART 2 = > Reverse the {num} number: {str(num)[::-1]}")
print(row_splitter)

print(row_splitter)
print(f"PART 3 = > Sort the digits in the {num} number: {''.join(sorted(str(num)))}")
print(row_splitter)
