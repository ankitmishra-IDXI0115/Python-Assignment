#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_words(a) :
    i=0
    k=0
    max_value=0
    result = []
    while i < len(a) :
        j=0
        count=0
        while j<len(a[i]) :
            count+=1
            j+=1
        result.append(count)
        i+=1

    while k < len(result) :
        if max_value<result[k] :
            max_value = result[k]
        
        k+=1
    return max_value

print(find_longest_words(['apple','car','watermelon']))                
 

   

