class Student:
    college_name = "PLU" 
    name = "anoynmous" #class attr


    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks
        print("let's see")

s1 = Student("Reven", 97)
print(s1.name)

# instance attibute takes precedence in usage when both have the same name
 