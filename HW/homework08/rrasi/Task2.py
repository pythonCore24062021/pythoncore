#Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
#В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
#В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи ‘@company.com’ наприкінці.

class Employee:
    def __init__(self, first_name, last_name, email="@company.com"):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = first_name + " " + last_name
        self.email = first_name + "." + last_name + email

    def __repr__(self):
        return self.fullname + ": " + self.email
user1 = Employee("ruslana", "yaniv")
print(user1)
