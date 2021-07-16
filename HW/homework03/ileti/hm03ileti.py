print("завдання 1")
python_philosophy = """"
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
print("counting words")
print(python_philosophy.count("better"))
print(python_philosophy.count("never"))
print(python_philosophy.count("is"))
print("Вивести весь текст у верхньому регістрі (всі великі літери)")
print(python_philosophy.title())
print("Замінити всі входження символу “і” на “&”")
print(python_philosophy.replace("i", "&"))

print("завдання 2")

import random
number =(random.randint(1000,9999))
number = str(number)
print("чотирицифрове натуральне число: " + number)
mult = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print(mult)

print("завдання 3")
a = 5
b = 10
print(a)
print(b)
a, b = b, a
print(a, b)

print('завдання 4')
var_int = 10
var_float = 8.4
var_str = "No"

var_big = var_int * 3.5
print(var_big)
var_float -= 1
print(var_float)
var_div1 = var_int / var_float
print(var_div1)
var_div2 = var_big / var_float
print(var_div2)
print(var_str + "NoYesYesYes")
