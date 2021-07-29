import random


class Door:
    def __init__(self, number, status, colour="red"):
        self.number = number
        self.status = status
        self.colour = colour

    def open(self):
        self.status = "opened"

    def close(self):
        self.status = "closed"
    def __del__(self):
        print("del:", self)
    def __str__(self):
        return f"{self.number=} {self.status=} {self.colour=}"
    def __repr__(self):
        return f"(N:{self.number} s:{self.status} {self.colour})"
    @staticmethod
    def stat(a,b,c):
        return a+b+c
    @classmethod
    def my_class_method(cls):
        print(type(cls), cls)

doors = []
for i in range(5):
    # door = Door(random.randint(1,99),
    #             ["opened", "closed"][random.randint(0,1)])
    door = Door(random.randint(1, 99),
                "opened" if random.randint(0, 1) else "closed")
    doors.append(door)
print(doors)
for door in doors:
    print(door)
print()
for door in doors:
    if door.number % 2:
        door.close()
for door in doors:
    print(door)
c = doors[4]
del doors[4]
del doors[3]
print(doors)
print(c)

c.__class__
c.my_class_method()
Door.my_class_method()

print(c.stat(1,2,3))
print(Door.stat(4,5,6))
