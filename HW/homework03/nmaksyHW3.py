# Завдання 1
my_str = 'Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren"t special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you"re Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it"s a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let"s do more of those!'

print(my_str.count("better"))
print(my_str.count("never"))
print(my_str.count("is"))
print(my_str.upper())
print(my_str.replace('i', '&'))
print('************************************')
# Завдання 2

n = input('Введіть чотиризначне число: ')
n = int(n)

d = n%10
c = n%100//10
b = n%1000//100
a = n//1000%100
print('Добуток цифр числа '+ str(n) + ':', a * b * c * d)

n = str(n)
str_lenth = len(n)
sliced_str = n[str_lenth::-1]
print(sliced_str)


ascending = "".join(sorted(n))
print(ascending)


descending = "".join(sorted(n), reverse=True)
print(descending)
print('************************************')
# Завдання 3

a =3; b = 5
print('a = ', a, '; b =', b, sep='')

a, b = b, a

print('a = ', a, '; b =', b, sep='')


print('************************************')
# Завдання 4

var_int = 10
var_float = 8.4
var_str = 'No'
var_int *= 3.5
var_big = var_int
var_float -= 1
var_div1 = var_int/var_float
var_div2 = var_big/var_float

var_str += 'NoYesYesYes'

print(var_int)
print(var_float)
print(var_str)
print(var_big)
print(var_div1)
print(var_div2)

