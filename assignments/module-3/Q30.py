# Write a Python program to unzip a list of tuples into individual lists.


tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]


list1, list2 = zip(*tuple_list)


list1 = list(list1)
list2 = list(list2)

print("First list:", list1)
print("Second list:", list2)
