# Write a Python function that:

# Takes an integer n
# # Returns:
# "Positive Even" if n is positive and even

# "Positive Odd" if n is positive and odd

# "Negative" if n is negative

# "Zero" if n is 0

# 📌 Rules:

# Use if / elif / else

# Use one function

# Do NOT use print inside the function (return only)

def OddEven(num) :
    if(num>0 and num%2==0):
        return "Positive Even"
    elif(num>0 and num%2!=0):
        return "Positive Odd"
    elif(num<0):
        return "Negative"
    else :
        return "Zero"
    
print(OddEven(-4))
