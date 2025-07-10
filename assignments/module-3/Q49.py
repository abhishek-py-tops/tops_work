# Write a Python function to calculate the factorial of a number (a nonnegative integer).

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))  
