#Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters
#contained in the file, and prints a sorted and nicely formatted character frequency table to the screen.

def char_freq_table():
    filename = input("Enter file name: ")

    freq = {}

    with open(filename, "r") as file:
        for line in file:
            for char in line:
                freq[char] = freq.get(char, 0) + 1

    # sort by character
    for char in sorted(freq):
        if char == "\n":
            display_char = "\\n"
        elif char == " ":
            display_char = "' '"
        else:
            display_char = char

        print(f"{display_char:>4} : {freq[char]}")
