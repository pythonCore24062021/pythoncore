p = 6
h = 10
num = int(input('Enter a number: '))
sum = 0
mult = 1
l_num = []

while num != p and num != h:
    if num < p:
        sum += num
    if num > h:
        mult *= num
    if p < num < h:
        l_num.append(num)
    num = int(input('Enter a number: '))

print(f'Sum is {sum}')
print(f'Multiplication is {mult}')
print("List of number between p and h:{0}".format(', '.join(map(str, l_num))))
