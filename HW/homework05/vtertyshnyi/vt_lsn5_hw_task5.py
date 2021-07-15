'''
5. Дано число P  і число H. Користувач вводить послідовність чисел. 
Визначити: 
- суму тих чисел, які менше P; 
- добуток чисел, які більші за H; 
- кількість чисел, що знаходяться в діапазоні значень від P до H.
При введенні числа рівного P або H, припинити обчислення та вивести результат. 
(не використовувати білдін функції)
'''

def get_num ():
    while True:
        try:
            num = int(input())
            break
        except ValueError:
            print("Oops... You should enter numbers only")
    return num

P = 10
H = 99
less_than_P = 0
greater_than_H = 0
between_P_H = 0

while True:
    print("Please enter some number:")
    n = get_num()
    if n == P or n == H:
        print("It's the end...")
        break
    if n < P:
        less_than_P += n
    elif n > H:
        if greater_than_H == 0:
            greater_than_H = n
        else:
            greater_than_H *= n
        #greater_than_H *= n if greater_than_H != 0 else greater_than_H = n
    else:
        between_P_H += 1
    
print(f"{less_than_P=}\
    \n{greater_than_H=}\
    \n{between_P_H=}")
