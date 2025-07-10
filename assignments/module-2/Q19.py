# Write a Python program to find the first appearance of the substring 'not' and 'poor' froma given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string.

text = input("Enter a sentence: ")

not_pos = text.find('not')
poor_pos = text.find('poor')

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
    
    result = text[:not_pos] + 'good' + text[poor_pos + 4:]
else:

    result = text


print("Result:", result)
