str = '''The Zen of Python, by Tim Peters
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!'''
print('str=', str)
print (str.count("better"))
print(str.count("never"))
print(str.count("is"))
'"Namespaces"'.upper()
s2 = str.lower()
print('s2=', s2)
s3 = str.upper()
print('s3=', s3)
substring = "better"
count = str.count(substring)
print("The count better is:", count)
replaced_string = str.replace('i', '&')
print('Replaced string:', replaced_string)

n2 = input("set number: ")
a = int(n2[0])
b = int(n2[1])
c = int(n2[2])
print("dobutok:", a*b*c)
n_list = list(n2)
n_list.reverse()
n3 = "".join(n_list)
print("reverse order:", n3)
n2 = input("set number: ")
a = int(n2[0])
b = int(n2[1])
c = int(n2[2])
n_sort = list(n2)
n_sort.sort()
print(n_sort)
a = 10
b = 20
a, b = b, a
print(a)
print(b)
