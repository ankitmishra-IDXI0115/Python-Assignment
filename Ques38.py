#Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the
#  text, divided by the number of word tokens).

def average_word_length(filename):
    total_len = 0
    total_words = 0

    with open(filename) as f:
        for line in f:
            words = line.split()
            total_words += len(words)
            total_len += sum(len(word) for word in words)

    return total_len / total_words
