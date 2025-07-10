# Write a python program to find the longest words.

file = open("example.txt", "r")

text = file.read()

file.close()

words = text.split()

max_length = max(len(word) for word in words)

longest_words = [word for word in words if len(word) == max_length]

print("Longest word(s):", longest_words)
print("Length:", max_length)
