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

# # n = int(input())
# # for i in range(2, n+1):
# #     if n % i == 0:
# #         break
# # if i == n:
# #     print("prime")
# # else:
# #     print("not prime")
print("hello world!")
# Recursive function for Fibonacci series
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print Fibonacci series up to n terms
def print_fibonacci_series(n):
    series = []
    for i in range(1, n+1):
        series.append(fibonacci(i))
    return series

# Example: Fibonacci series of 10 terms
print(print_fibonacci_series(23))