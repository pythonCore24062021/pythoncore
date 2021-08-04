num = int(input('Enter a number: '))
count = 0
count_plus = 0

while num != 0:
    count += 1
    if num > 0:
        count_plus += 1
    num = int(input("Enter a number: "))

print(f'Percentage of positive numbers is {count_plus*100/count:.4f}%')
print(f'Percentage of negative numbers is {(count-count_plus)*100/count:.4f}%')
