def is_prime(number):

    if number == 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

n = int(input("enter number from 0 to 1000 = "))
print(is_prime(n))
