#Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
#Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(s):
    freq = {}           
    i = 0

    while i < len(s):
        ch = s[i]

        if ch in freq:
            freq[ch] = freq[ch] + 1    
        else:
            freq[ch] = 1               

        i += 1

    return freq


print(char_freq("abbabcbdbabdbdbabababcbcbab"))
