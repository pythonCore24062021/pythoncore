# Task6

int1 = int(input('Please specify any number - '))
a = 0
b = 0
while int1 != 0:
    if int1 < 0:
        a += 1
    elif int1 > 0:
        b += int1
    int1 = int(input('Please specify any number - '))
else:
    print("Bingo")
    print(f"The percentage of negative numbers is equal to {a/(a+b)*100}% \n"
          f"The percentage of positive numbers is equal to {b/(a+b)*100}%")

