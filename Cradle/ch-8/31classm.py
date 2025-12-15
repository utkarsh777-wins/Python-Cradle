# Method1
class Person:
    name = "anonymous"

    def changeName(self, name):
        Person.name = name  #changed the name
        # Person.

p1 = Person()
p1.changeName("Siri")
print(p1.name)  
print(Person.name)
