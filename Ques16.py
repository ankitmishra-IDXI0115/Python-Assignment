#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
 
def filter_long_words(a, n):
    i = 0
    result = []

    while i < len(a):
        j = 0
        count = 0
        while j < len(a[i]):
            count += 1
            j += 1

    
        if count > n:
            result.append(a[i])
 
        i += 1

    return result

print(filter_long_words(['cat','apple','watermelon'],3))