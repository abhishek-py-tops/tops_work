# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Constructor to initialize radius

    def area(self):
        return math.pi * self.radius ** 2  # πr²

    def perimeter(self):
        return 2 * math.pi * self.radius  # 2πr

# ✅ Example usage:
c = Circle(5)

print("Radius:", c.radius)
print("Area:", c.area())           # Output: 78.53981633974483
print("Perimeter:", c.perimeter()) # Output: 31.41592653589793
