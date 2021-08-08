# Task 6
import random


def is_prime(n):
    if n == 1:
        print(f"{n} is a prime number")
    i = 1
    while i < n:
        i += 1
        if n % i == 0:
            print(f"{n} is a prime number")
            return True
        else:
            print(f"{n} is not a prime number")
            return False


print(is_prime(random.randint(0, 1000)))
