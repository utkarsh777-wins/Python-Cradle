# Class and Instance Attributes
'''
class attributes are common for the complete class
instance attributes --exclusive to the certain object
-- we use self. for instance/object attributed
--it's value will be different/varying for each instance

'''
class Student:
    college_name = "PLU" #class attribute
    def __init__(self, name, marks):
        self.name = name #instance attribute
        self.marks = marks
        print("Student Marks")

s1 = Student("Reven", "98")
print(s1.name, s1.marks)


s2 = Student("Riple", "99")
print(s2.name, s2.marks)
print(s2.college_name)
print(Student.college_name) #same value
# class attribute stored just once in the memory
# object attributes will be stored multiple times in the memory for different values
