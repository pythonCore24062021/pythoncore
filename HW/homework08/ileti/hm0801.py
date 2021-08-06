class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def compare_age(self, other):
        if self.age > other.age:
            print(f"{other.name} is younger than me ")
        elif self.age == other.age:
            print (f"{other.name} is the same age as me")
        else:
            print (f"{other.name} is older than me ")


p1 = Person(32, "John")
p2 = Person(28, "Max")
p3 = Person(24, "Troy")

print(p2.compare_age(p2))