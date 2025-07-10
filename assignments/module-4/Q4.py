# Write a Python program to read first n lines of a file.


n = 3

file = open("example.txt", "r")

for i in range(n):
    line = file.readline()
    if line == '':
        break  
    print(line.strip())  

file.close()
