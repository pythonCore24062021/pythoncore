#В класі Person визначте метод compare_age(), який повертатиме результат порівняння віку людини з Вашим віком.
#При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age, буде повертатися повідомлення наступного формату:
#{other_person} is {older than / younger than / the same age as} me.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"name:{self.name} age:{self.age}"
    def compare_age(self, person):
        if self.age < person.age:
            return f"{person.name} is older than {self.name}"
        if self.age > person.age:
            return f"{person.name} is younger than {self.name}"
        if self.age == person.age:
            return f"{person.name} is the same age as {self.name}"
my = Person("Ruslana", 25)
p1 = Person("Ruslana1", 15)
p2 = Person("Ruslana2", 25)
p3 = Person("Ruslana3", 35)
print(my)
print(p1)
print(p2)
print(p3)
print(my.compare_age(p1))
print(my.compare_age(p2))
print(my.compare_age(p3))




