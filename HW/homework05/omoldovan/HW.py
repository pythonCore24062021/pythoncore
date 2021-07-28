# 2 Task
'''
counter = 0
counter_number = 0
while counter < 10:
    number = int(input("Vvedit naturlne chyslo bilshe 2: "))
    if number < 2:
        print(f"{number}<2")
        continue
    else:
        counter += 1

    if number % 5 == 0:
        counter_number = counter_number + 1
    print(f"{counter_number}")

'''

# Task 3
'''for i in range(1, 10):
    for j in range(1, 10):
        if j < 9:
            print(f"{i}*{j}", end=",")
        else:
            print(f"{i}*{j}\n")'''


# Task 4 ---- подивитися ще розв'язки
'''a = int(input("Vvedit vysotu priamokutnyka: "))
b = int(input("Veedit dovzynu primokutnyka: "))
print("It look like")
for i in range(a):
    if i == 0 or i == (a-1):
        for j in range(b):
            print("*", end="")
    else:
        print("*", end="")
        for j in range(b-1):
            print("#", end="")
        print("*", end="")
    print()'''

# Task 5
'''sum_ = 0
dob = 1
count = 1
H = int(input("Enter a 'H' value: "))
P = int(input("Enter a 'P' value: "))
range_of_numbers = None
while range_of_numbers != P or range_of_numbers != H:
    range_of_numbers = int(input("Enter any value: "))
    if range_of_numbers == P or range_of_numbers == H:
        print("Stop the program")
        break
    elif range_of_numbers < P:
        sum_ = sum_ + range_of_numbers
    elif range_of_numbers > H:
        dob = dob*range_of_numbers
    elif range_of_numbers in range(H, P):
        count = count + 1
    print(f"The sum of number under 'P'= {P} is {sum_}. The multiple of numbers above the 'H'= {H} is {dob}."
          f" The amount of number in range between the 'H'= {H} and 'P'= {P} is {count}")
print(f"The sum of number under 'P'= {P} is {sum_}. The multiple of numbers above the 'H'= {H} is {dob}."
      f" The amount of number in range between the 'H'= {H} and 'P'= {P} is {count}")'''

# Task 6
'''counter_plus = 0
minus_count = 0
numbers = None
while numbers != 0:
    numbers = int(input("Enter a value: "))
    if numbers == 0:
        print("Stop the program")
        break
    elif numbers < 0:
        minus_count = minus_count + 1
    else:
        counter_plus = counter_plus + 1
        one_percent = (counter_plus + minus_count) / 100
        dodatni = counter_plus / one_percent
        vidjemni = minus_count / one_percent
print(f"The percent of >0 is {round(dodatni,2)}.The percent of < 0 is {round(vidjemni,2)}")'''

# Task 1

import random
chyslo = random.randint(0, 100)

for i in range(10, 0, -1):
    answer = int(input("Vhadai chyslo: "))
    if i == 0 and answer != chyslo:
        print (f"You lose. The answer is {chyslo}")
        break
    if answer == chyslo:
        print(f"Congratulations, you won. The answer is {chyslo}")
        break
    elif answer < chyslo:
        print(f"The secret number is higher. You have {i} lives")
    else:
        print(f"The secret number is lower. You have {i} lives")
