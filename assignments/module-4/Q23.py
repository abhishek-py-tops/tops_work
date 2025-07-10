# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length      # Constructor to initialize length
        self.width = width        # and width

    def area(self):
        return self.length * self.width  # Area = length × width

# ✅ Example usage:
r = Rectangle(10, 5)

print("Length:", r.length)
print("Width:", r.width)
print("Area of Rectangle:", r.area())  # Output: 50
