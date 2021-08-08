# Task1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age > my_age:
            print(f"{self.name} is older than me")
        elif self.age < my_age:
            print(f"{self.name} is younger than me")
        else:
            print(f"{self.name} is the same age as me")

my_age = 37
p1 = Person("Roman", 37)
p2 = Person("Olia", 25)
p3 = Person("Joey ", 70)
Person.compare_age(p1, my_age)
Person.compare_age(p2, my_age)
Person.compare_age(p3, my_age)