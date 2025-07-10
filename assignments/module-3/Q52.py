# Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))       
