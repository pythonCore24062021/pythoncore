# class A:
#     def f(self, a):
#         print("f: ", self, a)
#
# def g(ob, a):
#     print(ob, a)
#
# a = A()
# a.f(28)
# print(type(a.f), id(a.f))
# g(a, 28)
#
# k = A.f
# print(type(k), id(k))
# k(a, 55)
# A.m = g
# a.m(99)

# class A:
#     def __init__(self):
#         self.p = "pu"
#         self._pr = "pr"
#         self.__pri = "private"
#     def __print__(self):
#         print(f"{self.p=} {self._pr=} {self.__pri=}")
# a= A()
# a._pr
# a.__print__()
# print(a._A__pri)

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        point = Point()
        point.__x = self.__x + other.__x
        point.__y = self.__y + other.__y
        return point

    def __radd__(self, other):
        self.__x += other
        self.__y += other

    def __str__(self):
        return f"x:{self.__x} y:{self.__y}"

    def __float__(self):
        return float(f"{self.__x}.{self.__y}")

    def __get_x(self):
        print(f"get x:{self.__x} {self.__class__}")
        return self.__x

    def __set_x(self, x):
        if not type(x) == int:
            print("bad x")
            return None
        self.__x = x
        print(f"set x:{self.__x} {self.__class__}")

    x = property(__get_x, __set_x)

    @property
    def y(self):
        print(f"get y:{self.__y} {self.__class__}")
        return self.__y
    @y.setter
    def y(self, y):
        if not type(y) == int:
            print("bad y")
            return None
        self.__y = y
        print(f"set y:{self.__y} {self.__class__}")


# p1 = Point(1,2)
# p2 = Point(4,7)
# p3 = p1 + p2
# print(p1)
# print(p2)
# print(p3)
# 4+p3
# print(p3)
# print(float(p3))

#
# p1 = Point(1, 2)
# p1.x = "vdfshbvjhd"
# p1.x
# p1.y
# p1.y = 20
# p2 = Point(4, 7)
# print(p1)
# print(p2)
# p3 = p1 + p2
# print(p1.x)

class Point3D(Point):
    def __init__(self, x=1, y=1, z=1):
        super().__init__(x, y)
        self.__z = z

    @property
    def z(self):
        print(f"get y:{self.__z} {self.__class__}")
        return self.__z

    @z.setter
    def z(self, z):
        if not type(z) == int:
            print("bad y")
            return None
        self.__z = z
        print(f"set y:{self.__z} {self.__class__}")

    def __str__(self):
        return f"x:{self.x} y:{self.y} z:{self.__z}"
    def print_2d(self):
        print(super().__str__())
p3d = Point3D(1,4)
p3d.x = 5
p3d.y
print(p3d)
p3d.print_2d()
