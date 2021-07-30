# Task 1

"""
class Person:

    def compare_age(self, name, age):
        your_age = int(input("Enter your age: "))
        if age > your_age:
            print(f"{name} is older than me")
        elif age < your_age:
            print(f"{name} is younger than me")
        else:
            print(f"{name} is the same age as me")



p1 = Person()
p1.compare_age('olx',21)
p2 = Person()
p2.compare_age('BTS', 0)
p3 = Person()
p3.compare_age("Ivan", 12)


#!!!!!!!!!!!!!!!!!  p4 = Person.compare_age()  --- why this doesn't work?  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

# Task 2
"""

class Employee:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def fullname_creation(self):
        fullname = self.first_name + " " + self.last_name
        print(f"The fullname is {fullname}")
        return fullname
    
    def email_creation(self):
        email = self.first_name+ "." + self.last_name + "@company.com"
        print(f"The email is {email}")
        return email
    
    
em1 = Employee("Oleksandr", "Moldovan")
em1.fullname_creation()
em1.email_creation()

"""

# Task 3

'''
class Name:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        fullname = fname + " " + lname
        initials = fname[0] + "." + lname[0] + "."
        print()
        print(f"{fullname}, \n{initials}")


a = Name("Olek", "Moldovan")
b = Name("Gevorgh", "Sacybelli")

'''