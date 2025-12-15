'''
A class method is bound to the class & receives 
the class as an implicit first arguement

Note - static method can't access or modify class
state & generally for utility.

class Student:
    @classmethod    #decorator
    def college(cls):
        pass

'''
class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.__class__.name = "Siri"
    @classmethod
    def changeName(cls, name):  #cls-referring to the class
        cls.name = name

p1 = Person()
p1.changeName("Siri-chan")
print(p1.name)  
print(Person.name)
