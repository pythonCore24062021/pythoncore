'''
1. У програмі генерується випадкове ціле число від 0 до 100. 
Користувач повинен його відгадати не більше ніж за 10 спроб. 
Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число,
ніж те, що загадане. Якщо за 10 спроб число не відгадане, то вивести загадане число.
'''

from random import randint

def get_answer ():
    while True:
        try:
            answer = int(input())
            break
        except ValueError:
            print("Oops... You should enter numbers only!")
    return answer

num_to_guess = randint(0, 100)
num_of_attempts = 10
print(f"Hi! \
    \nI've thought of a number and want you to guess it in {num_of_attempts} attempts, could you? \
    \nThan just enter you guess here ...")

for i in range(num_of_attempts, 0, -1):
    last_answer = get_answer()
    if last_answer == num_to_guess:
        print(f"You've done it in {num_of_attempts - i + 1} attempt(s)! Great work!")
        break
    elif i != 1:
        print(f"Nope, that's not the right number, but you still have {i-1} attempt(s).\
            \nAnd small hint - ", end='')
        
        if last_answer < num_to_guess:
            print("your number is less than my.")
        else:
            print("your number is greater than my.")
        
        if last_answer < 0 or last_answer > 100:
            print("Btw, my number is in [0; 100] range, I've told you previously, haven't I?\
                \nIsn't a great way to loose an attempt... but you did it!")

        print("So your next choisee is:")
else:
    print(f"So sad ... the number was {num_to_guess}. \
        \nWho knows, maybe next time ... :) ")