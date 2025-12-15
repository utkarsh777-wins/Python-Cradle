# Property Decorator
''''
We use @property decorator on any method in the class
to use the method as a property

'''
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3 ) + "%"

    # def calculatePercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3 ) + "%"

stu1 = Student(12,31,33)
print(stu1.percentage)

stu1.phy = 66
print(stu1.percentage)