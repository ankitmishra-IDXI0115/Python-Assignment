#Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. 
# (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

""">>> import guess_number
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!"""


import random

def guess_number():
    number = random.randint(1, 20)
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
