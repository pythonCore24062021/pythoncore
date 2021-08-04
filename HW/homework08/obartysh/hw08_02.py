class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.email = name + "." + surname + "@company.com"

    def represent(self):
        return self.fullname + ": " + self.email


p1 = Employee("Haruma", "Miura")
p2 = Employee("Sherlock", "Holms")
p3 = Employee("James", "Moriarty")

print(p1.represent())
print(p2.represent())
print(p3.represent())