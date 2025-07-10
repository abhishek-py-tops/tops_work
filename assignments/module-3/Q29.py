# Write a Python program to remove an empty tuple(s) from a list of tuples.


tuple_list = [(), (1, 2), (), (3,), (4, 5), (), ()]

filtered_list = [t for t in tuple_list if t]

print("List after removing empty tuples:", filtered_list)
