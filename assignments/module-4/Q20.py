# Write python program that user to enter only odd numbers, else will raise an exception.

try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
        raise ValueError("You entered an even number. Only odd numbers are allowed!")
    print("Thank you! You entered an odd number:", num)
except ValueError as e:
    print("Exception:", e)
