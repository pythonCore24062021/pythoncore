#Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
#В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
#В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи ‘@company.com’ наприкінці.

class Employee:
    def __init__(self, fullname, email):
        self.fullname = fullname
        self.email = email
    def __str__(self):
        return f"name:{self.name} age:{self.age}"
    def compare_age(self, person):
        if self.age < person.age:
            return f"{person.name} is older than {self.name}"
        if self.age > person.age:
            return f"{person.name} is younger than {self.name}"
        if self.age == person.age:
            return f"{person.name} is the same age as {self.name}"
my = Person("Ruslana", 25)
p1 = Person("Ruslana1", 15)
p2 = Person("Ruslana2", 25)
p3 = Person("Ruslana3", 35)
print(my)
print(p1)
print(p2)
print(p3)
print(my.compare_age(p1))
print(my.compare_age(p2))
print(my.compare_age(p3))