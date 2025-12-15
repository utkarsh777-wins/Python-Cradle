class Person:
    __name = "anonymous"

    def __hellow(self):
        print("mellow")

    def welcome(self):
        self.__hellow()

# only methods within the class can access private attributes




p1 = Person()

# print(p1.__name)
# print(p1.__hellow)
print(p1.welcome())