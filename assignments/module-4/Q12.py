# Write a Python program to copy the contents of a file to another file.

source_file = open("source.txt", "r")

destination_file = open("destination.txt", "w")

for line in source_file:
    destination_file.write(line)

source_file.close()
destination_file.close()

print("File copied successfully.")
