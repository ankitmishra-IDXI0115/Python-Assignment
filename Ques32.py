#Write a version of a palindrome recogniser that accepts a file name from the user, reads each line,and prints the line to the screen if it is a
#palindrome.

def is_palindrome(line):
    # remove non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in line if char.isalnum())
    return cleaned == cleaned[::-1]


filename = input("Enter file name: ")

with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        if is_palindrome(line):
            print(line)
