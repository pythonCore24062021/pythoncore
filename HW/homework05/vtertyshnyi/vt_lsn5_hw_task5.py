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
lessThanP = 0
greaterThanH = 0
betweenPH = 0

while True:
    print("Please enter some number:")
    n = get_num()
    if n == P or n == H:
        print("It's the end...")
        break
    if n < P:
        lessThanP += n
        continue
    elif n > H:
        if greaterThanH == 0:
            greaterThanH = n
        else:
            greaterThanH *= n
        #greaterThanH *= n if greaterThanH != 0 else greaterThanH = n
        continue
    else:
        betweenPH += 1
    
print(f"{lessThanP=}\n{greaterThanH=}\n{betweenPH=}")
