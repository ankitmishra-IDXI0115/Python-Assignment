#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

def wordslength(words) :
    i=0
    result=[]
    while i<len(words):
        count =0
        j=0
        while j < len(words[i]) :
            count+=1
            j+=1
        result.append(count)
        i+=1
    return result

print(wordslength(['apple','ball','cycle']))
