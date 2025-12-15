# Private(like) attributes and methods
'''
Conceptual Implementaation in Python
Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

add __ in frontof attributes or methods makes them private


'''

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Grey")        #public
print(s1.name)
print(s1)   