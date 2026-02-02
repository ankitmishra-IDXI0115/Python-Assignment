#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
#Write it in three different ways:
#1) using a for-loop 
#2) using the higher order function map()
#3) using list comprehensions.

def wordsintointegersforloop(a) :
    #1 USING FOR LOOP

   lengths = []
   for word in a:
        lengths.append(len(word))
   return lengths

def wordsintointegersmap(a) :
      return list(map(len, a))


def wordsintointegerslistcomprehensions(a) :
        return [len(word) for word in a]
     

a = ["apple", "banana", "cherry", "kiwi"]
print(wordsintointegersforloop(a))
print(wordsintointegerslistcomprehensions(a))
print(wordsintointegersmap(a))