my_age = 29


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def compare_age(self):
        if self.age > my_age:
            text = "older than"
        elif self.age < my_age:
            text = "younger than"
        else:
            text = "the same age as"
        return f'{self.name} is {text} me'


person1 = Person("Adam West", 30)
person2 = Person("John Doe", 29)
person3 = Person("Alanis Morissette", 27)

print(person1.compare_age)
print(person2.compare_age)
print(person3.compare_age)
