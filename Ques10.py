#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
# You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested 
# for-loops.

def overlapping(a,b) :
    i=0
    
    while i<len(a):
        j=0
        while j<len(b) :
            if a[i] == b[j] :
                return True
            else :
                j+=1
        i+=1
    return False    

print(overlapping(['a','o','c'],['o','d','e']))        

