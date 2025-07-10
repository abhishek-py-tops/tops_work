#  Write a Python program to count the number of characters (character frequency) in a string


user_string = input("Enter a string: ")

char_frequency = {}


for char in user_string:
    if char in char_frequency:
        char_frequency[char] += 1 
    else:
        char_frequency[char] = 1   


print("Character Frequency:")
for char, count in char_frequency.items():
    print(f"'{char}': {count}")

