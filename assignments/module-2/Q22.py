# Write a Python program to get a string made of the first 2 and the last 2
#chars from a given a string. Ifthe string length islessthan 2,return instead of the empty string.
 #Sample String:w3resource'
 #Expected Result: 'w3ce'
 #Sample String: 'w3'
 #Expected Result: 'w3w3'
 #Sample String: ' w'
 #Expected Result: Empty String


def first_and_last_2_chars(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]


print(first_and_last_2_chars('w3resource'))  
print(first_and_last_2_chars('w3'))          
print(first_and_last_2_chars('w'))           
