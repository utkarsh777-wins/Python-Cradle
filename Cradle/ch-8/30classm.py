# types of methods:
'''
-instance method(self)
-class method(cls)  @classmethod
-static method  @staticmethod

'''

# class method
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("Siri")
print(p1.name)  #created a new name
print(Person.name)
# not the change we wanted through instance method