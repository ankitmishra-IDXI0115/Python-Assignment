#According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" 
#spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user and finds and prints all
#pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list,
#the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!

filename = input("Enter file name: ")

with open(filename, "r") as file:
    words = [line.strip() for line in file]

word_set = set(words)

for word in words:
    reversed_word = word[::-1]

    if reversed_word in word_set and word != reversed_word:
        print(word, reversed_word)
        word_set.remove(word)
        word_set.remove(reversed_word)
 