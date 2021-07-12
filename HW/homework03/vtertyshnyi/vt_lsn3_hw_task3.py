row_splitter = '\n' + '#' * 100 + '\n'

print(row_splitter)
print("PART 1 => swap two variables without third one")

a = ('str1', 47, {4, 5, 7})
b = {5, 'str2'}

print(f"Initial: {a} and {b}")

a, b = b, a

print(f"Switched: {a} and {b}")
print(row_splitter)
