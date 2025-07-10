# Write a Python program to map two lists into a dictionary.

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Mumbai']


mapped_dict = dict(zip(keys, values))

print("Mapped Dictionary:", mapped_dict)
