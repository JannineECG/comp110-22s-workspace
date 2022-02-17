"""Ex02 - One Shot Wordle."""

__author__ = "730470181"

secret: str = "python"

guess: str = str(input("What is your 6-letter guess?"))

checking: int = 0

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8" 

line: str = ""
maybe: bool = False
other: int = 0

while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again:")
if guess != secret:
    print(line)
    print("Not quite. Play again soon!")
else:
    if guess == secret:
        print(line)
        print("Woo! You got it!")

while checking < len(secret):  
    if guess[checking] == secret[checking]:
        line = line + green_box
    else:
        while not maybe and other < len(secret):
            if secret[other] == guess[checking]:
                maybe = True
            else:
                other = other + 1
        if maybe:
            line = line + yellow_box
        else:
            line = line + white_box
    checking = checking + 1
    other = 0
    maybe = False