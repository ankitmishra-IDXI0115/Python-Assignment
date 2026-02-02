#Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns
#the list of words that are longer than n.

def filter_long_words(words,n):

    return list(filter(lambda word: len(word) > n, words))


words = ["apple", "banana", "cherry", "kiwi"]
print(filter_long_words(words,5))
