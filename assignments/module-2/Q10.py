#  Write a Python program that will return true ifthe two given integervalues are equal or their sum or difference is 5.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


if a == b or a + b == 5 or abs(a - b) == 5:
    print("Result: True")
else:
    print("Result: False")
