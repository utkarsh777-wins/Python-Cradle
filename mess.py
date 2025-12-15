# circle area and perimeter
import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"

# Usage
c1 = Circle(3)
print(c1)                  # Circle(radius=3)
print("Area:", c1.area())  # Area: 28.274333882308138
print("Perimeter:", c1.perimeter())  # Perimeter: 18.84955592153876