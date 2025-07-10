#  Write a Python program to test whether a passed letter is a vowel or not.


letter = input("Enter a single letter: ").lower()


if len(letter) == 1 and letter.isalpha():
    
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(f"The letter '{letter}' is a vowel.")
    else:
        print(f"The letter '{letter}' is not a vowel.")
else:
    print("Invalid input. Please enter a single alphabet letter.")
