# start = 0
# end = 10
# while start < end:
#     print(start, end="=>")
#     start += 1
#     print(start, end, start < end)
# else:
#     print (f"{start=} {end=}")


# start = 0
# end = 10
# while start < end:
#     print(start, end="=>")
#     start += 1
#     if start == end:
#         end += 5
#     print(start, end, start < end)
# else:
#     print (f"{start=} {end=}")

# start = 10
#
# while start:
#     print(start, end="=>")
#     start -= 3
#     print(start)
# else:
#     print (f"{start=}")

# start = "abcd"
#
# while start:
#     print(start, end="=>")
#     start = start[:-1]
#     print(start)
# else:
#     print (f"{start=}")

# start = 0
# end = 10
# while start < end:
#     _start = 0
#     while _start < end:
#         print(start, _start)
#         _start += 1
#     start += 1
#
# print(f"{start=} {_start=}")


# start = 10
# end = 10
# while start < end:
#     _start = 0
#     while _start < end:
#         print(start, _start)
#         _start += 1
#     start += 1
#
# print(f"{start=} {_start=}")


# for i in range(10):
#     print(i)

# l = (1, 2, 3, 4)
# for i in l:
#     print(i)
#     l = l + l
# print(l)

# l = [1, 2, 3, 4]
# for i in l:
#     print(i)
#     l.append(1)
# print(l)

# def f(n):
#     print("func n=", n)
#     return [1, 2, 3]
#
#
# for i in f(5):
#     print(i)


# start = 1
# end = 4
# while start < end:
#     for ch in "abcde":
#         # print(start, ch)
#         for c in "!@#$%^":
#             print(start, ch, c)
#     start += 1

# start = 1
# end = 4
# while start < end:
#     print(start)
#     for ch in "abcde":
#         print(f"\t{ch}")
#         for c in "!@#$%^":
#             print(f"\t\t{c}")
#     start += 1
# print(c)

# def f():
#     print("f: ",dir())
#     a = 10
#     print("f: ",dir())
#     print(a)
# print(dir())
# f()
# stat=10
# print(dir())
# print(a)

# start = 0
# end = 10
# while start < end:
#     print(start)
#     if start == 5:
#         start +=2
#         continue
#     start += 1
# else:
#     print("else")
# start = 0
# end = 10
# while start < end:
#     print(start)
#     if start == 5:
#         start += 2
#         break
#     start += 1
# else:
#     print("else")
# print(start)


# for i in range(10):
#     if i % 2:
#         print(i ** 3)
#         continue
#     print(i)
#     if i >7:
#         break
# else:
#     print("else", i)

# for i in range(5):
#     print(i)
#     for j in range(5):
#         print("\t", j)
#         if i == j:
#             break
#         print("\t\t", i, j)

# for i in range(5):
#     print(i)
#     for j in range(5):
#         print("\t", j, end="")
#         if i == j:
#             print()
#             continue
#         print("\t", i, j)
#
# a = 1
# for i in range(10):
#     pass
#
#
# print(a)

# import random
# for i in range(10):
#     a = random.randint(0, 100)
#     print(a)

from random import randint
for i in range(10):
    a = randint(0, 100)
    print(a)

import imp
from imp import name, age
print(imp.name)
print(imp.age)
print(age)
print(name)

# ****
# *##*
# ****