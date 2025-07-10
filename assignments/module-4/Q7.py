# Write a Python program to read a file line by line store it into a variable.

file = open("example.txt", "r")

content = ""
for line in file:
    content += line

file.close()

print(content)
