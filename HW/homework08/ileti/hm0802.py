class Employee:
    def __init__(self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name

    def fullname (self):
        fullname = self.first_name + "-" + self.last_name
        return fullname

    def create_mail (self):
        emailbox= self.first_name + "." + self.last_name + "@company.com"
        return emailbox

emp_1 = Employee ("Ira","Letiy" )
emp_2 = Employee ("Fabian","Otto" )
emp_3 = Employee ("Adrian","Burlacu" )

print(emp_1.fullname())
print(emp_1.create_mail())