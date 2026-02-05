
# Write a function that:
# Takes a string
# Returns the number of vowels (a, e, i, o, u)
# Case-insensitive (A and a both count)
# Do NOT use regex


def VowelCounter(a) :
    a=a.lower()
    vowels = "aeiou"
    count =0
    for char in a :
        if char in vowels :
            count+=1
    return count

print(VowelCounter("hEllo i am ankIt"))