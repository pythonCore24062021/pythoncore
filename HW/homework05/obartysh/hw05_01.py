import random

print("Try to guess a number between 1 and 100 in less than 10 tries")
number = random.randint(1,100)
count = 0
while count < 10:
    guess = int(input("enter a number: "))
    count += 1
    if guess < number:
        print("too low.")
    elif guess > number:
        print("too high.")
    elif guess == number:
        print(f"You did it in {count} tries.")
    if count == 10:
        print(f"You didn't guess the number. the number was: {number}")
