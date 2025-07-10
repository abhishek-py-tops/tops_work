# Write a Python program to replace last value of tuples in a list.

tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_list = [t[:-1] + (100,) for t in tuple_list]


print("Updated list of tuples:")
print(new_list)
