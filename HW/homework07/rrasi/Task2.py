#2. Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True,
#якщо рік високосний, і False в іншому випадку.

def CheckYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
year = int(input("Enter Year: "))
if(CheckYear(year)):
    print("Leap Year")
else:
    print("It is not a Leap Year")