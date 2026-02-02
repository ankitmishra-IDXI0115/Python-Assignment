#Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def is_vowel(char):
    return char.lower() in ['a', 'e', 'i', 'o', 'u']


print(is_vowel("a"))