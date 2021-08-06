'''
6. Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000, 
   і повертає True, якщо воно просте, і False - в іншому випадку.
'''

def is_prime(num):
    try:
        num = int(num)
        if num == 0: raise Exception("Zero value...")
        if num < 0 or num > 1000: raise Exception("Out of range! Must be in (0;1000]")
    except ValueError:
        return "Parameter must be a number"
    except Exception as msg:
        return msg
    
    div = num
    while (div != 1) and (div != 2): 
        div -= 1
        if num % (div):
            continue
        else:
            return False        
    else:
        return True

# test
for i in range(-1, 10):
   print(f"is_prime({i}) = {is_prime(i)}")