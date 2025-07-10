# Write a Python program to read last n lines of a file.


n = 3

file = open("example.txt", "r")

lines = file.readlines()

for line in lines[-n:]:
    print(line.strip())

file.close()
