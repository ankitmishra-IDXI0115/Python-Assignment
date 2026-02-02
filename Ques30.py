#Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
#"new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish.
#Use the higher order function map() to write a function translate() that takes a list of English words and returns a list of Swedish words.

def translate(words):
    return list(map(lambda word: lexicon[word], words))

lexicon = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
"new":"nytt", "year":"år"}

english = ["merry", "christmas", "and", "happy", "new", "year"]
swedish = translate(english)
print(swedish)

