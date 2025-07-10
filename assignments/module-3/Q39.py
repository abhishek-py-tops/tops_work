# Write a Python program to check multiple keys exists in a dictionary

my_dict = {'name': 'Alice', 'age': 25, 'city': 'Mumbai', 'gender': 'Female'}

keys_to_check = ['name', 'age', 'city']

if all(key in my_dict for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("One or more keys are missing.")
