#6. Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000, і повертає True,
#якщо воно просте, і False - в іншому випадку.

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "True is not a prime number"
            else:
                return "False is a prime number"
num = int(input("Enter a number: "))
print(is_prime(num))