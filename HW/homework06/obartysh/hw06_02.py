entered_list = []
sum_list = 0
mult_list = 1
n = int(input("enter a number of elements in the list "))

for i in range(0, n):
    entered_list.append(int(input('Enter number: ')))
    sum_list += entered_list[i]
    mult_list *= entered_list[i]

print(f'List: {entered_list}')
print(f'Sum of numbers in the list: {sum_list}')
print(f'Multiplication of numbers in the list: {mult_list}')
