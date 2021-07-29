'''
2. Вводяться десять натуральних чисел більше 2. 
Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)
'''

def get_num (_not_less_than):
    while True:
        try:
            num = int(input())
            if num <= _not_less_than: raise Exception(f"Number should be greater than {_not_less_than}")
            break
        except ValueError:
            print("Oops... You should enter numbers only")
        except Exception as msg:
            print(msg)
    return num

not_less_than = 2
multiples_of = 5
sum = 0

for i in range(10):
    print(f"Enter the {i+1} number:")
    num = get_num(not_less_than)
    if num % multiples_of == 0:
        sum += num
    
print(f"Summary of the multiples of {multiples_of} is {sum}")
