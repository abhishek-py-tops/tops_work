# Write a Python function to get the largest number, smallest num and sum of all from a list.

def list_summary(numbers):
    if not numbers:
        return None, None, 0  
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    return largest, smallest, total


nums = [10, 5, 20, 7]
largest, smallest, total = list_summary(nums)

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum:", total)
