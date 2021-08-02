from random import randint

def get_user_input_numbers ():
    while True:
        try:
            answer = int(input())
            break
        except ValueError:
            print("Oops... You should enter numbers only!")
    return answer

def get_user_input_float ():
    while True:
        try:
            answer = float(input())
            break
        except ValueError:
            print("Oops... You should enter numbers only!")
    return answer

def get_random_list (length = 20, min_val = -100, max_val = 100):
    # populate list with random items:
    my_list = [
        randint(min_val, max_val) 
        for i in range(length)
        ]
    return my_list