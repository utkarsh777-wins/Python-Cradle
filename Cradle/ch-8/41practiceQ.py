class Circle: 
    def __init__(self, radius):
        self.r = radius
        print("Circle of radius", self.r)

    def Area(self):
        print(f"Area of circle of {self.r} is: {(22/7) * self.r * self.r}")
    
    def Perimeter(self):
        print(f"Perimeter of circle of {self.r} is: {2 * (22/7) * self.r}")

c1 = Circle(21)
c1.Area()
c1.Perimeter()