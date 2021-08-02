class MyFirstClass:
    populations = 0
    def __init__(self, name, age=18):
        MyFirstClass.populations += 1
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name=} {self.age=}"
    def __eq__(self, other):
        print(f"__eq__({self}, {other})")
        return True
    def my_print(lf):
        print("my:", lf)


a1 = MyFirstClass("a1")
a2 = MyFirstClass("a2", 10)
a3 = MyFirstClass("a3", age=25)
# print(a1)
# print(a2)
# print(a3)
# a1.my_print()
#
# print(dir())
# print(type(a1), id(a1))
# print(type(MyFirstClass), id(MyFirstClass))
#
# # MyFirstClass.aaa = 22
# # print(MyFirstClass.aaa)
# print(dir(MyFirstClass))
# print(MyFirstClass.__dict__)
# print(dir(a1))
# print(a1.__dict__)
#
#
# def my_print(lf):
#     print("my:", lf)
# t = MyFirstClass.my_print
# t("foo")
# my_print("boo")
#
# print(a1 == a2)
print(MyFirstClass.__dict__.keys())
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
a3.name = "A3"
print(a3.__dict__)
a1.my_print()
MyFirstClass.my_print(a1)
print(MyFirstClass.populations)
print(a1.populations)
print(a2.populations)