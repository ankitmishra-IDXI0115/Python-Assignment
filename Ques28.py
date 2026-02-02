#Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.

from functools import reduce

def find_longest_word(words):
    return reduce(lambda x, y: x if x > y else y,map(len, words))


words = ["apple", "banana", "cherry", "kiwi"]
print(find_longest_word(words))