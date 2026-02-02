#A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an 
#author, or in a single text. Define a function that given the file name of a text will return all its hapaxes.
#Make sure your program ignores capitalization.

def hapax(filename):
    freq = {}

    with open(filename) as f:
        for line in f:
            for word in line.lower().split():
                freq[word] = freq.get(word, 0) + 1

    return [word for word in freq if freq[word] == 1]
