'''
3. Написати функцію square, яка приймає 1 аргумент - сторону квадрата, 
   і повертає 3 значення (за допомогою кортежу): 
    - периметр квадрата, 
    - площу квадрата 
    - і діагональ квадрата.
'''

def square(side):
    try:
        side = int(side)
    except ValueError:
        return "Side must be a number"
    p = side * 4 
    s = side ** 2
    d = side * (2**0.5)
    return (p, s, d)


print(square(10))
print(square('b'))