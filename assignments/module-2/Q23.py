# Write a Python function to insert a string in the middle of a string.

def insert_middle(main_str, insert_str):
    mid = len(main_str) // 2  
    return main_str[:mid] + insert_str + main_str[mid:]


print(insert_middle("hello", "123"))       
print(insert_middle("Python", "Fun"))      
