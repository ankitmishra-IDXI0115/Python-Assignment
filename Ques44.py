#Your task in this exercise is as follows:

"""Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), 
none of which mis-nest.
Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK"""

import random

def is_balanced(s):
    balance = 0
    for ch in s:
        if ch == '[':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def generate_and_check(n):
    s = '[' * n + ']' * n
    s = ''.join(random.sample(s, len(s)))
    print(s, "OK" if is_balanced(s) else "NOT OK")
