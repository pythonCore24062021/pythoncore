# n = 5
# m = 5
#
# matrix = [[j * i for j in range(m)] for i in range(n)]
# print(matrix)
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end="\t")
#     print()
#
# n = 10
# m = 7
# matrix = [[j * i for j in range(m)] for i in range(n)]
# print(matrix)
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end="\t")
#     print()

#
# def print_matrix(mat, rows_number, columns_number):
#     for i in range(rows_number):
#         for j in range(columns_number):
#             print(mat[i][j], end="\t")
#         print()
#     print()
#
#
# def print_all_matrix(mat):
#     for i in range(len(mat)):
#         for j in range(len(mat[i])):
#             print(mat[i][j], end="\t")
#         print()
#     print()
#
#
# def generate_matrix(rows_number, columns_number):
#     # return [[j * i for j in range(columns_number)] for i in range(rows_number)]
#     matrix = []
#     for i in range(rows_number):
#         row = []
#         for j in range(columns_number):
#             row.append(j * i)
#         matrix.append(row)
#     return matrix
#
#
# n, m = 5, 5
# matrix1 = generate_matrix(n, m)
# print_matrix(matrix1, n, m)
#
# n, m = 3, 8
# matrix2 = generate_matrix(n, m)
# print_matrix(matrix2, n, m)
#
# print_all_matrix(matrix1)
# print_all_matrix(matrix2)
#
# matrix3 = [
#     [1, 2, 3],
#     [4, 5],
#     [6, 7, 8, 9],
#     [10]
# ]
# print_all_matrix(matrix3)
#
# def print_foo():
#     """
#     print string foo
#     :return: str -> "foo"
#     """
#     print("foo")
#     return "foo"
#
# f = print_foo()
# print(f)
# help(print_foo)
# help(print_foo.__doc__)


# ## Required arguments
# def func(a, b):
#     print(f"a:{a} b:{b}")
#     return (a + b, a * b, a ** b)
# print(func(2, 3))
# # print(func())
#
# ##Keyword arguments
# print(func(2, 3))
# print(func(3, 2))
# print(func(a=3, b=2))
# print(func(b=3, a=2))

##Default arguments

# def func(a, b=9):
#     print(f"a:{a} b:{b}")
#     return (a + b, a * b, a ** b)
# print(func(3))
# print(func(3, 2))
# print(func(b=3, a=2))
#
# def func2(a,c, b=1):
#     pass
# func(1,2,3,4)

## Variable-length arguments
# def func(a, *ar, b=11, c=22, **kw):
#     print(f"a:{a} args:{ar} b:{b} {c=} {kw=}")
#
# func(1, 2)
# func("b", b=1)
# func(1, 2, 3, 4, 5, b=1, c=2, d=3)

# def func(a, b, c, d, *args, **kwargs):
#     print(f"{a=} {b=} {c=} {d=} {args=} {kwargs=}")
#
#
# func(1, 2, 3, 4)
# l = [11, 22, 33, 44]
# func(l[0], l[1], l[2], l[3])
# func(*l)
# l = [11, 22, 33, 44, 55]
# func(*l)
# d = {
#     "b": "bb",
#     "a": "a",
#     "c": "CCC",
#     "d": "DdD",
# }
# func(*d)
# func(**d) #func(a = d.get("a"), b=d["b"])
# d = {
#     "b": "bb",
#     "a": "a",
#     "c": "CCC",
#     "d": "DdD",
#     "dd": "DdD",
#     "ddd": "DdD",
# }
# func(**d)
# func(**d)


# ## Scope
# g = "gl"
# print(dir())
# def my_f():
#     a = 1
#     b = []
#     print(g)
#     print(dir())
# my_f()
#
# print(dir())

# gi = "gl"
# gm = [1,2,3]
#
# def my_f():
#     gi = 15
#     gm.append(11)
#     print(gi)
#     print(gm)
# my_f()
# print(gi)
# print(gm)

# gi = "gl"
#
# def my_f():
#     global gi
#     print(gi)
#     gi = 15
#
#     print(gi)
# my_f()
# print(gi)

# def f(a):
#     r =[1,2,3]+[1]
#     a = r
#     print(r, id(r), id(a))
# t =1
# f(t)
# print(t, id(t))
# f(t)
# print(t, id(t))
# f(t)
# print(t, id(t))

# # import sys
# # sys.setrecursionlimit(99999)
# def calc_factorial(x, st=""):
#     s = f"{x}*calc_factorial({x - 1})"
#     i = st.find("*calc")
#     if x == 1 or x == 0:
#         s = st[:i] + f"*1"
#         print(s)
#         return 1
#
#     else:
#
#         s = st[:i] + f"*{x}*calc_factorial({x-1})"
#         print(s)
#         return x * calc_factorial(x - 1, s)
#
#
# print(calc_factorial(10))


def f(a, b):
    return  a**b

print(f(2,3))
k = f
print(k(2,3))

f = lambda a, b: a**b; print("lambda")
print(f(2,3))
print(f(2,3))

