# Write a Python program to returns sum of all divisors of a number.

def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total


num = 12
print(f"Sum of all divisors of {num} = {sum_of_divisors(num)}")
