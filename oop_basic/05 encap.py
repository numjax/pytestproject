# - *- coding: utf- 8 - *-

class Person:
    DEFAULT_LIMIT_AGE = 20

    def __init__(self,name, age):
        self.age = age
        self.name = name

    def check_age(self):
        return self.age >= Person.DEFAULT_LIMIT_AGE


class Hof:
    pass

class Pup:
    pass

person1 = Person("kim", 20)
person2 = Person("lee", 18)

print (person1.check_age())
print (person2.check_age())