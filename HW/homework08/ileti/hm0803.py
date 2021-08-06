
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name= last_name

    def fname(self):
        return self.first_name

    def lname(self):
        return self.last_name

    def fullname(self):
        return self.first_name + self.last_name

    def initials(self):
        return self.first_name[1].upper() + "." + self.last_name[1].upper()


name1 = Name("Haruma", "Miura")
name2 = Name("Sherlock", "Holms")
name3 = Name("James", "Moriarty")

print(name1.fname())
print(name1.lname())
print(name1.fullname())
print(name1.initials())
