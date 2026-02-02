#Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). 
# For example, is_palindrome("radar") should return True.

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("radar"))