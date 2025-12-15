class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def calculatePercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3 ) + "%"
    @property                   #automatic updation
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3 ) + "%"

stu1 = Student(12,31,33)
print(stu1.percentage)

stu1.phy = 66
print(stu1.percentage)
# attribute value : function 
# => making the attribute property