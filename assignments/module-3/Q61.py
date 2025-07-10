# Write a Python program to read a random line from a file.

import random

def read_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()  
        if not lines:
            return "File is empty."
        return random.choice(lines).strip()  

file_name = 'example.txt'  
print("Random line:", read_random_line(file_name))
