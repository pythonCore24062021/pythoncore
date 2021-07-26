
my_number = int(input('Enter a number: '))
count = 0
plus_count = 0

while my_number != 0:
    count += 1
    if my_number > 0:
        plus_count += 1
    my_number = int(input("Enter a number: "))

print(f'We have {plus_count*100/count:.4f} % of positive numbers')
print(f'We have {(count-plus_count)*100/count:.4f} % of negative numbers')