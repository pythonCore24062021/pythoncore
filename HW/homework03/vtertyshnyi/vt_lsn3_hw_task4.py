row_splitter = '\n' + '#' * 100 + '\n'

var_int = 10
var_float = 8.4
var_str = "No"

print(row_splitter)
print("PART 1 => Initial values:")
print("\t- var_int =", var_int)
print("\t- var_float =", var_float)
print("\t- var_str =", var_str)
print(row_splitter)

var_big = var_int * 3.5
var_float -= 1
var_div1 = var_int / var_float
var_div2 = var_big / var_float
var_str = var_str * 2 + 'Yes' * 3

print(row_splitter)
print("PART2 => Chaged values:")
print("\t- var_int =", var_int)
print("\t- var_big =", var_big)
print("\t- var_float =", var_float)
print("\t- var_div1 =", var_div1)
print("\t- var_div2 =", var_div2)
print("\t- var_str =", var_str)
print(row_splitter)
