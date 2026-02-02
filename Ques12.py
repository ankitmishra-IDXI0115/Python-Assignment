#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7])
#  should print the following:

#****
#*********
#*******
def histogram(a):
    i = 0
    while i < len(a):
        j = 0
        while j < a[i]:
            print("*", end="")
            j += 1
        print()  
        i += 1

print(histogram([13,4,5]))
