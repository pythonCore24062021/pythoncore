# Задано чотирицифрове натуральне число.

# Знайти добуток цифр цього числа.
number = '6174'
print(int(number[0]) * int(number[1]) * int(number[2]) * int(number[3]))
# Записати число в реверсному порядку.
print(int(number[3]+number[2]+number[1]+number[0]))
# Посортувати цифри, що входять в дане число
ascending = "".join(sorted(str(number)))
print(int(ascending))
