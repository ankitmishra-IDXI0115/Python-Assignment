# Write a function that:
# Takes a list of integers
# Returns a new list containing squares of only odd numbers
# Do NOT modify the original list
# Do NOT use list comprehension (we’ll do that later)

def squareList(n):
    list1 = []
    for i in n :
        if i%2!=0 :
            list1.append(i*i)
        else : 
            continue
    return list1

num = [1,2,3,4,5,6,7]
print(squareList(num))