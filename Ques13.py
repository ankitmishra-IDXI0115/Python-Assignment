#The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. 
# But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() 
# that takes a list of numbers and returns the largest one.

def maxfinder(a) :
    i=0
    max = a[0]
    while i<len(a) :
        if a[i] > max :
            max = a[i]
        i+=1    
    
    return max

print(maxfinder([2,9,5,0,12,15,3,8]))
