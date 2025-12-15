# Method2
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = "Siri"
        # self.__class__.

p1 = Person()
p1.changeName("Siri-chan")
print(p1.name)  
print(Person.name)
