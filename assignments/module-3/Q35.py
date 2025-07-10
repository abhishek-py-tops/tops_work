# Write a Python script to check if a given key already exists in a dictionary.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

key_to_check = 'age'

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
