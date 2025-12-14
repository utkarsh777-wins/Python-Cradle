class Student:
    # default constructors 
    def __init__(self):
        pass

    # parametarised constructors
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
        print("Student Marks")

s1 = Student("Reven", "98")
print(s1.name, s1.marks)


s2 = Student("Riple", "99")
print(s2.name, s2.marks)

# either we make these default constructrs or python does automatically in case if we don't
#generally we don't need multiple constructors