# Write a Python program to get the Fibonacci series of given range.

n = int(input("Enter the number of terms: "))

a, b = 0, 1


if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci series:")
    print(a)
else:
    print("Fibonacci series:")
    print(a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
