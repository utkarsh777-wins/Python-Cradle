class Student:
    college_name = "PLU"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("welcome student")

s1 = Student("Kaiser", 91)
s1.welcome()