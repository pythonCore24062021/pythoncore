my_age = int(input("enter your age "))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self):
        if self.age > my_age:
            text = "older than "
        elif self.age < my_age:
            text = "younger than "
        else:
            text = "the same age as "
        return f'{self.name} is {text} you'

p1 = Person("Haruma Miura", 30)
p2 = Person("Sherlock Holms", 35)
p3 = Person("James Moriarty", 40)

print(p1.compare_age())
print(p2.compare_age())
print(p3.compare_age())
