# Task1
# Generate a random number up to 100
import random
a=(random.randint(0,100))
int1=int(input(f"Guess a number from 0 to 100 ... \n"))

# Build a guessing loop
start=10
while start > 0:
    if int1 < a:
        print("Almost there, but the number is bigger")
        int1 = int(input(f"Try again! Guess a number from 0 to 100 ... \n"))
        start -=1
        continue
    elif int1 > a:
        print("You are so close, but the number is lower")
        int1 = int(input(f"Try again! Guess a number from 0 to 100 ... \n"))
        start -= 1
        continue
    elif int1 == a:
        print(f"Bingo!!! the number is '{int1}'")
        break
else:
    print("you have spent all yours attempts")