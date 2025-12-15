# del keyword
# used to delete object properties or the entire object itself
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Grey")
print(s1.name)
del s1.name
print(s1)       #won't raise an error
# print(s1.name)
# AttributeError: 'Student' object has no attribute 'name'      