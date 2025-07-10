# Write a Python program to calculate surface volume and area of a cylinder.

import math

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

# Example 
r = 5
h = 10

surface_area = cylinder_surface_area(r, h)
volume = cylinder_volume(r, h)

print(f"Surface Area of cylinder = {surface_area:.2f}")
print(f"Volume of cylinder = {volume:.2f}")
