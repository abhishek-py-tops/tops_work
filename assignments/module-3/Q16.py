# Write a Python program to get unique values from a list.

def get_unique_values(input_list):
    unique_values = list(set(input_list))
    return unique_values

my_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = get_unique_values(my_list)
print("Unique values:", unique_list)
