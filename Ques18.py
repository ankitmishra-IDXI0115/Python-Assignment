#A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over
#the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.


def is_pangram(sentence):
    i = 0
    letters = []

    
    while i < len(sentence):
        ch = sentence[i]

        
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)

        
        if ch >= 'a' and ch <= 'z':
            
            found = False
            j = 0
            while j < len(letters):
                if letters[j] == ch:
                    found = True
                    break
                j += 1

            if not found:
                letters.append(ch)

        i += 1

    
    if len(letters) == 26:
        print("pangram")
    else:
        print("not a pangram")
