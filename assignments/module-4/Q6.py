# Write a Python program to read a file line by line and store it into a list.


file = open("example.txt", "r")

lines = [line.strip() for line in file]

file.close()

print(lines)
