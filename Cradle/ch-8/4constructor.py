# Constructor

'''
__init__ Function
All classes have a function called __init__(), which is always executed when the object is being initiated.

--the self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

--even if we don't write an init function python will automatically create and execute it --there will always be a constructor for us.

--constructor always takes an argument/parameter --self


'''
class Student:
    name = "Chloe"
    def __init__(self):
        print(self)
        print("Registering the new students to our database")

#calls the contructor
s1 = Student()    
print(s1) 
# <__main__.Student object at 0x0000017337AC6F90> 
# same location as when print self