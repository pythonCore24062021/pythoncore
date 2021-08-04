# Task 1
'''
def arithmetic(a, b, operation):
    # a = int(input("Enter a value 'a'"))
    # b = int(input("Enter a value 'b'"))
    # operation = input("Enter an operation")
    if operation == '+':
        res = a+b
        print(f"Result is: {res}")
        return res
    elif operation == '-':
        res = a-b
        print(f"Result is: {res}")
        return res
    elif operation == '/':
        res = a/b
        print(f"Result is: {res}")
        return res
    elif operation == '*':
        res = a*b
        print(f"Result is: {res}")
        return res
    else:
        print("Unknown operation")

arithmetic(1,2,'f')
'''

'''
#Task 2
def is_year_leap(year):
    """This dunction define if year is a leap_year"""
    if year %4 == 0:
        print("True")
        return True
    else:
        print("False")
        return False

is_year_leap(2000)
'''

# Task 3
'''
def square(square_side):
    P = square_side*4
    S = square_side**2
    D = square_side*2**0.5
    res = (P,S,D)
    print(f"The results are: Perimetr, Square, Diametr {res}")
    return res
square(3)
'''
# Task 4
'''
def season(month_number):
    "Find the season according to the month number"
    if month_number <=0 or month_number> 12:
        print("Month with such number not exist")
    elif month_number in (1,2,12):
        print("The season is winter")
    elif month_number in (3,4,5):
        print("The season is spring")
    elif month_number in (6,7,8):
        print("The season is summer")
    else:
        print("The season is autumn")
season(4)
'''

# Task 5
"""
def bank(money_amount, years):
     total = money_amount + money_amount / 10
     for i in range(years+1):
         total = total + total / 10
         print(f"The ${total} will be in your count in {i} years")
    #total = round(money_amount*((1+0.1/1)**(1*years)),2)
bank(1000,5)
"""

# Task 6
"""
def is_prime(number):
    a = None
    b = None
    number_list = [3, 5, 2, 7]
    for i in number_list:
        if number <=0 or (number//i >1 and number%i==0):
            a = False
        else:
            b = True
    if a == False:
        print("False")
    else:
        print("True")

is_prime(15)
"""

#Task 7
"""
def date(day,month,year):
    _31_day_month=[1,3,5,7,8,10,12]
    _30_day_month=[4,6,9,11]
    if (year%4==0 and year>= 0) and month == 2 and day<=29 and day>0:
        print("True")
    elif (year%4!=0 and year>=0) and month == 2 and day<=28 and day>0:
        print("True")
    elif year>=0 and (month in _31_day_month and day<=31 and day>0) or (month in _30_day_month and day<= 30 and day>0):
        print("True")
    else:
        print("False")
date(12,12,0)
"""