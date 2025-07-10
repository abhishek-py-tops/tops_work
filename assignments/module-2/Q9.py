#  Write a Python program to sum of three given integers.However if two values are equal sum will be zero.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a == b or b == c or a == c:
    print("Two or more values are equal. Sum is 0.")
    total = 0
else:
    total = a + b + c
    print(f"Sum of the numbers is: {total}")
