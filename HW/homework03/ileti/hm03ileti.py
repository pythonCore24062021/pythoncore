######1
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
print(python_philosophy.count("better", "never", "is"))
print(python_philosophy.title())
print(python_philosophy.replace("i", "&"))

####2
number = "4536"
dobutok = number[0:5]
dobutok = number[0] * number[1] * number[2] * number[3]
print("Добуток чотиризначного числа: " + dobutok)
print(f"Для цього числа {number} Визначте добуток чисел {dobutok})


#####3
a=5
b=10
print(a)
print(b)

a,b  = b, a
print ("value a: " + a)
print ("value b: " + b)

######4

Змініть значення, збережене в змінній var_int, збільшивши його в 3.5 рази, результат надайте змінній var_big.
Змініть значення, збережене в змінній var_float, зменшивши його на одиницю, результат надайте тій же змінній.
Розділіть var_int на var_float, а потім var_big на var_float. Результат запишіть у змінні var_div1 та var_div2 відповідно.
Змініть значення змінної var_str на "NoNoYesYesYes". При формуванні нового значення використовуйте операції конкатенації (+) і повторення рядка (*).


var_int=10
var_float=8.4
var_str="No"