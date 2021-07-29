class Name:
    def __init__(self, name, surname):
        self.name = name
        self.lname = surname
        self.fullname = name + " " + surname
        self.initials = name[1].upper() + "." + surname[1].upper()

    def __repr__(self):
        return self.fullname + ": " + self.initials


name1 = Name("Adam", "West")
name2 = Name("John", "Doe")
name3 = Name("Alanis", "Marionette")

print(name1)
print(name2)
print(name3)
