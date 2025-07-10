#  Write a python program to sum of the first n positive integers.


n = int(input("Enter a positive integer: "))


if n > 0:
    
    total = n * (n + 1) // 2
    print(f"Sum of the first {n} positive integers is: {total}")
else:
    print("Please enter a positive integer.")
