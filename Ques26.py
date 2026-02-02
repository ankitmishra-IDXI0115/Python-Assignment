#Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. 
# Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?

from functools import reduce

def max_in_list(x, y):
    if x > y:
        return x
    else:
        return y

a = [1, 2, 3, 4, 6, 5]
result = reduce(max_in_list, a)
print(result)
