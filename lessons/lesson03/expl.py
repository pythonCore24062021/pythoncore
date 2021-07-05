a = 99 ** 9999

# print(a)
# print(id(a))
# a = a-1
# a = a+1
# print(id(a))
# print(id(a+1-1))
#
# print(len(str(a)))
# print(type(a))
# a = 5
# print(id(a), a)
# a += 5
# print(id(a), a)
# l = [1]
# print(id(l), l)
# l.append(1)
# print(id(l), l)
# l.append(1)
# print(id(l), l)
# str1 = "1234"
# str1 = str1[:1] + 'c' + str1[2:]
# print(str1, str1[1])
#
# l = [1, "", [1, {1, 2, 3}], 1.5]
# print(l)
#
# class A:
#     pass
#
# a = A()
# print(type(a))
# print(a)
# print(id(a))
# print(int("0x00000248EBD66F70", 16))
# print(2512217599856)

### int
# a = 1
# b = int()
# print(a, b)
# a = int("111")
# # b = int("a51")
# # b = int("0123456789")
# b = int("100", 2)
# # b = int("100.5")
# b = int("z", 36)
# print(a, b)
# 01
# 012
# 0123
# 0123456789a
# 0123456789a..z
#
# print((-2)**0.5)
#
# print(float("5.5"))
# for i in range(300):
#     print(i, "\t", chr(i))
#
# print("&", ord("&"))
# str1 = "11'1"
# str2 = '11"1'
# str3 = "0123456789abcd"
# print(len(str3))
# print(str3)
# print(str3[11])
# print(str3[3:11])
# print(str3[3:11:3])
# print(str3[3:110:3])
# print(str3[:9])
# print(str3[5:])
# print(str3[-1])
# print(str3[-2])
# print(str3[-5:])
# print(str3[-5:5])
# print(str3[-5:5:-1])
# l = [1,2,3]
# name = "John"
# age = 23
# print(name +" is " + str(age) + "years old.")
# print("%s is %d years old. " % (name, age))
# print("{} is {} years old. ".format(name, age))
# print("{0} is {1} years old. {1} is {0} years old. ".format(name, age))
# print("{k1} is {k2} years old. {k2} is {k1} years old. ".format(k1=name, k2=age))
# print(f"{name} is {age} years old. {l}")
print([m for m in dir(str) if not m[0] == "_"])
# help(str.title)
#
# str1 = "abc abc. abc abc."
# print(str1.capitalize())
# print(str1.center(50))
# print(str1.count("ab"))
# print(str1.count("abz"))
# print(str1.endswith("c."))
# print(str1.endswith("sc."))
# print(str1.index("c."))
# print(str1.index("c.", 7))
# # print(str1.index("c.", 16))
# print(str1.find("c."))
# # print(str1.find("c.", 80))
# str1 = "     abc abc. abc abc.       "
# print(str1)
# print(str1.strip())
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.upper())
# print(str1.title())
# l = ["1", "2", "3", "4", "5"]
# s = "<->".join(l)
# print(s)
# s2 = "1<->2<->3<->4<->5"
# print(s2.split("<-"))
# print(s2.zfill(30))
# print(s2.replace("<", "**", 2))
# print(7/3)
# print(7//3)
# print(7%3)
# print(8//5)
# print(8%5)
# print(5**(1/3))

import math
a = 123.58
print(math.trunc(a,))
print(math.floor(a))
print(int(a))
