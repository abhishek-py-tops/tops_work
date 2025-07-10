# Write a Python program to write a list to a file.


items = ["apple", "banana", "cherry", "mango"]

file = open("fruits.txt", "w")

for item in items:
    file.write(item + "\n")

file.close()

print("List has been written to fruits.txt")
