# Task 3

class Name:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.fullname = first_name + " " + last_name
        self.initials = first_name[0] + "." + last_name[0]

    def show_data(self):
        return f"the full name is {self.fullname} \nthe initials are: {self.initials}"


name1 = Name("Nick", "Paterson")
name2 = Name("Roman", "Khodorovych")
name3 = Name("Unknown", "Person")

print(name1.show_data())
print("_______________")
print(name2.show_data())
print("_______________")
print(name3.show_data())
