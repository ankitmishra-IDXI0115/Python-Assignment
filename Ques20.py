#Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", 
# "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. 
# That is, write a function translate() that takes a list of English words and returns a list of Swedish words.


def translate(words):
    dictionaries = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    i =0
    result = []
    while i<len(words):
        if words[i] in dictionaries :
            result.append(dictionaries[words[i]])
            
        else :
            result.append(words[i])
        i+=1
    return result
print(translate("merry christmas and happy new year".split()))
