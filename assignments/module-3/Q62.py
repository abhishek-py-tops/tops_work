# Write a Python program to convert degree to radian.


import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = 180
radian = degree_to_radian(degree)
print(f"{degree} degrees = {radian:.4f} radians")
