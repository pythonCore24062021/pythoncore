row_splitter = '\n' + '#' * 100 + '\n'

num_a = 10
num_b = 55

print(row_splitter)
print(f"PART 1 => switch two variables without third one: {num_a} and {num_b}")
num_a += num_b
num_b = num_a - num_b
num_a = num_a - num_b 
print(f"Switched: {num_a} and {num_b}")
print(row_splitter)

# VT Open Questions: 
# - What about other types?!!! 
