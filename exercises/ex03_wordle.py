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
    where: int = 0
    line: str = ""
    while where < len(secret):
        if guess[where] == secret[where]:
            line = line + green_box
        else:
            if contains_char(secret, guess[where]):
                line = line + yellow_box
            else:
                line = line + white_box 
        where = where + 1
    return line


def input_guess(many: int) -> str:
    """Right characters."""
    guess: str = input(f"Enter a {many} character word:")
    while len(guess) != many:
        guess = input(f"That wasn't {many} chars! Try again:")
    else:
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    secret: str = "codes"
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        state: str = input_guess(len(secret))
        print(emojified(state, secret))
        if state == secret:
            print("You won in " + str(turns) + "/6 turns!")
            turns = turns + 6 
        elif state != secret and turns == 6: 
            print("X/6 - Sorry, try again tomorrow!")
        turns = turns + 1
            

if __name__ == "__main__":
    main()
