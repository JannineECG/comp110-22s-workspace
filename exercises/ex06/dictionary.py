"""EX06 - Dictionary Functions."""

__author__ = "730470181"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    result = dict()
    for key in a:
        value = a[key]
        if value in result:
            raise KeyError
        result[value] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:   
    """Returns the most popular color."""
    result = str()
    fave: dict[str, int] = {}
    i: int = 0
    for key in colors:
        color = colors[key]
        if color in fave:
            fave[color] += 1
        else:
            fave[color] = 1
    for color in fave:
        if fave[color] > i:
            i = fave[color]
            result = color
    return result


def count(val: list[str]) -> dict[str, int]:
    """Number of times a word appears."""
    end: dict[str, int] = dict()
    for v in val:
        if v in end:
            end[v] += 1
        else:
            end[v] = 1
    return end
