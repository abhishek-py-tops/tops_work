# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

# Example 
decimal_numbers = [3.5, 7.2, 1.8, 9.4, 2.6]

max_num, min_num = find_max_min(decimal_numbers)

print(f"Maximum number = {max_num}")
print(f"Minimum number = {min_num}")
