class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.email = name + "." + surname + "@company.com"

    def __repr__(self):
        return self.fullname + ": " + self.email


person1 = Employee("Adam", "West")
person2 = Employee("John", "Doe")
person3 = Employee("Alanis", "Morissette")

print(person1)
print(person2)
print(person3)
