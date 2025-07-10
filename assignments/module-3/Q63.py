# Write a Python program to calculate the area of a trapezoid.

def area_of_trapezoid(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

b1 = 10
b2 = 6
h = 4

area = area_of_trapezoid(b1, b2, h)
print(f"Area of trapezoid = {area}")
