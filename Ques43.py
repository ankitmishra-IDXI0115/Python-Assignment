#An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the 
# original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, 
# write a program that finds the sets of words that share the same characters that contain the most words in them.

from collections import defaultdict

def largest_anagram_sets(words):
    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)

    max_size = max(len(v) for v in groups.values())
    return [v for v in groups.values() if len(v) == max_size]
