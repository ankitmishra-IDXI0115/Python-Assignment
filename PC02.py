
# Write a function that:
# Takes a list of numbers
# Returns count of even numbers
# Do NOT use len() or list comprehension

def EvenNumCounter(n) :
    count=0
    for i in n :
        if i % 2 == 0:
            count+=1
    return count

num = [2,3,4,5,6,7,8,9]
print(EvenNumCounter(num))