#Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.",
#  "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", 
# "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization,
#  and spacing are usually ignored.

def checkbigpalindrome(a):
    i = 0
    cleaned = ""

     
    while i < len(a):
        ch = a[i]

         
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            
            if ch >= 'A' and ch <= 'Z':
                cleaned += chr(ord(ch) + 32)
            else:
                cleaned += ch
        i += 1

     
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            print("not a palindrome")
            return
        left += 1
        right -= 1

    print("palindrome")


checkbigpalindrome("radar Ono Radar")


