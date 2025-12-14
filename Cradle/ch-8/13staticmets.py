# Static Methods
'''
Methods that don't use the self parameter(work at class level)
@staticmethod   #decorator
"Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it"

'''
class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    # def hello():      self doesn't make much sense here
    #     print("hello")
    #     Student.hello() takes 0 positional arguments but 1 was given

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hii!", self.name, "your avg score is:", sum/3)


s1 = Student("Toby", [33, 38, 31])
s1.get_avg()
# s1.hello()

s1.name = "spiderman" 
s1.get_avg()