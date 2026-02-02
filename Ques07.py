#Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string 
# "gnitset ma I"

def reverse(text):
    result = ""
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    return result

 