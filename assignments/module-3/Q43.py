# Write a Python program to print all unique values in a dictionary.

my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20,
    'f': 40
}

unique_values = set(my_dict.values())

print("Unique values in the dictionary:")
for value in unique_values:
    print(value)
