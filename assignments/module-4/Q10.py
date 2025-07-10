# Write a Python program to count the frequency of words in a file.

file = open("example.txt", "r")

text = file.read()

file.close()

words = text.lower().split()


word_freq = {}


for word in words:
    
    word = word.strip(".,!?;:\"'()[]{}")
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


for word, count in word_freq.items():
    print(f"{word}: {count}")
