#Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# m=max_of_three(3,8,5)
print(max_of_three(3,8,5))