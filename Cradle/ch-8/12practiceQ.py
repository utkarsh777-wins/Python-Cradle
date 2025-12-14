# create a student class that takes name&marks of 3subjects 
# as arguements  in constructor.
#then create a method to print the average
class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hii!", self.name, "your avg score is:", sum/3)


s1 = Student("Toby", [33, 38, 31])
s1.get_avg()

s1.name = "spiderman" #can directly change the value ofs1name
s1.get_avg()
