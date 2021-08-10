# Task2

class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.email = str.lower(first_name + "." + last_name + "@company.com")


employee1 = Employee("Nick", "Paterson")
employee2 = Employee("Roman", "Khodorovych")
employee3 = Employee("Unknown", "Person")

print(employee1.email)
print(employee1.full_name)
print(employee2.email)
print(employee2.full_name)
print(employee3.email)
print(employee3.full_name)
