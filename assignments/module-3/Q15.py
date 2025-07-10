# Write a Python program to find the second smallest number in a list.

def second_smallest(numbers):
    if len(numbers) < 2:
        return None  

    unique_numbers = list(set(numbers))  

    if len(unique_numbers) < 2:
        return None  

    unique_numbers.sort()
    return unique_numbers[1]  

my_list = [4, 1, 7, 2, 1, 5]
result = second_smallest(my_list)

if result is not None:
    print("Second smallest number:", result)
else:
    print("Second smallest number not found.")
