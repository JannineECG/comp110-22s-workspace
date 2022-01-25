"""Ex01 - Chardle - A cute step toward Wordle."""

__author__ = "730470181"

special_word: str = str(input("Enter a 5-character word: "))
if len(special_word) != 5:
    print("Error: word muct contain 5 characters")
    exit()

char_1: str = input("Enter a single character:")
if len(char_1) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + char_1 + " in " + special_word)

count: int = 0

if special_word == int(4 < 5):
    print("Error: word must contain 5 characters")

if char_1 == special_word[0]:
    print(char_1 + " found at index 0")
    count = count + 1
if char_1 == special_word[1]:
    print(char_1 + " found at index 1 ")
    count = count + 1
if char_1 == special_word[2]:
    print(char_1 + " found at index 2")
    count = count + 1
if char_1 == special_word[3]:
    print(char_1 + " found at index 3")
    count = count + 1
if char_1 == special_word[4]:
    print(char_1 + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + char_1 + " found in " + special_word)
if count == 1:
    print("1 instance of " + char_1 + " found in " + special_word)
if count == 2:
    print("2 instance of " + char_1 + " found in " + special_word)
if count == 3:
    print("3 instance of " + char_1 + " found in " + special_word)
if count == 4:
    print("3 instance of " + char_1 + " found in " + special_word)
if count == 5:
    print("5 instance of " + char_1 + " found in " + special_word)
