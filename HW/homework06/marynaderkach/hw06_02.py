entered_list = []
sum = 0
mult = 1

for i in range(0, 5):
    entered_list.append(int(input('Enter number: ')))
    sum += entered_list[i]
    mult *= entered_list[i]

print(f'List: {entered_list}')
print(f'Sum of numbers in the list: {sum}')
print(f'Multiplication of numbers in the list: {mult}')
