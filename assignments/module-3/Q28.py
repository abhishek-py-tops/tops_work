# Write a Python program to find the repeated items of a tuple.

my_tuple = (1, 2, 3, 2, 4, 5, 6, 1, 7, 8, 3, 3)

repeated_items = set()
seen = set()

for item in my_tuple:
    if item in seen:
        repeated_items.add(item)
    else:
        seen.add(item)

print("Repeated items in the tuple are:", repeated_items)
