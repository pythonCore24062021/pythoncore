import random

print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in five tries or less")

my_number = random.randint(1, 100)
tries = 0

while tries < 10:
    guess = (input('Guess a number: '))
    tries += 1
    if not guess.isnumeric() or (100 <= int(guess) or int(guess) <= 0):
        print("Please enter number between 1 and 100")
    else:
        guess = int(guess)
        if guess < my_number:
            print('Your guess is too low.')
        elif guess > my_number:
            print('Your guess is too high.')
        elif guess == my_number:
            print(f'You guessed my number in {tries} tries.')
            break
    if tries == 10:
        print(f'I was thinking about: {my_number}')
