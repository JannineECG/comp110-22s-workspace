"""Ex03-wordle-Structured Wordle."""

__author__ = "730470181"


def contains_char(where: str, n: str) -> bool:
    """A string being searched."""
    assert len(n) == 1
    depends: bool = False
    here: int = 0
    while here < len(where):
        if n == where[here]:
            depends = True 
            return depends
        else:
            here = here + 1
    return depends


def emojified(guess: str, secret: str) -> str:
    """A string being searched resulting emojis."""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    depends: bool = False
    here: int = 0
    check: int = 0
    line: str = ""
    while here < len(secret):
        if guess[here] == secret[here]:
            line = line + green_box
        else:
            while not depends and check < len(secret):
                if secret[check] == guess[depends]:
                    depends = True 
                else:
                    check = check + 1 
            if depends: 
                line = line + yellow_box
            else:
                line = line + white_box
        here = here + 1
        check = 0
        depends = False
    return line


def input_guess(many: int) -> str:
    """Right characters."""
    guess: str = str(input(f"Enter a {many} character word:"))
    while len(guess) != many:
        guess = input(f"That wasn't {many} chars! Try again:")
    if len(guess) == many:
        print(guess)
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    secret: str = "codes"
    counter = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        state: str = input_guess(len(secret))
        print(emojified(state, secret))
        turns = turns + 1
        if state == secret:
            print("You won in " + str(counter + 1) + "/6 turns!")
            exit()
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
