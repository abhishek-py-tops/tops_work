# Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word_length(word_list):
    
    longest = max(word_list, key=len)
    return len(longest)

words = ["apple", "banana", "grapefruit", "kiwi"]
print("Length of the longest word:", longest_word_length(words))
