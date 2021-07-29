class Name:
    def __init__(self, name, surname):
        self.name = name
        self.surnamename = surname
        self.fullname = name + " " + surname
        self.initials = name[0].upper() + "." + surname[0].upper()

    def represent(self):
        return self.fullname + ": " + self.initials

p1 = Name("Haruma", "Miura")
p2 = Name("Sherlock", "Holms")
p3 = Name("James", "Moriarty")

print(p1.represent())
print(p2.represent())
print(p3.represent())
