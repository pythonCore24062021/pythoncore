import random
tries = 0
number = random.randint(1, 100)
print ('Try to guess the number from 1 to 100')
while tries < 10:
    guess = int(input('Take a guess: '))
    tries += 1
    if guess < number:
        print(('Your guess is too low'))
    if guess > number:
        print(('Your guess is too high'))
    if guess == number:
        print(f'Congratulations! You guessed my number in {tries} guesses')
        break
    if guess != number and tries == 10:
        print(f'Sorry, game over. My number was {number}')
        break