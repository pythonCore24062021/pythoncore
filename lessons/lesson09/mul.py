# class A():
#     def print(self):
#         print("A", end=" ")
#
#     def print1(self):
#         print("A1", end=" ")
#
#     def print2(self):
#         print("A2", end=" ")
#
#     def print3(self):
#         print("A3", end=" ")
#
#     def print4(self):
#         print("A4", end=" ")
#
#
# class B(A):
#     def print(self):
#         print("B", end=" ")
#
#     def print1(self):
#         print("B1", end=" ")
#
#     def print2(self):
#         print("B2", end=" ")
#
#
# class C(A):
#     def print1(self):
#         print("C1", end=" ")
#     def print2(self):
#         print("C2", end=" ")
#
#     def print3(self):
#         print("C3", end=" ")
#
#
# class D(B, C):
#     pass
# class E(C, B):
#     pass
#
#
# l = [A(), B(), C(), D(), E()]
#
# for i in l:
#     print(i.__class__)
#     print(i.__class__.__mro__)
#     i.print()
#     i.print1()
#     i.print2()
#     i.print3()
#     i.print4()
#     print()

class A:pass
class B(A):pass
class C(A):pass
class D(A):pass
class E(B):pass
class F(B):pass
class G(D):pass
class J(F):pass
class Z(J,G,E,C):pass

print(Z.__mro__)
