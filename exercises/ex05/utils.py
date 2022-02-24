"""Ex05 - utils."""

__author__ = "730470181"


def only_evens(lis: list[int]) -> list[int]:
    """Construct a list of only even numbers."""
    eve: list[int] = list()
    i: int = 0
    while i < len(lis):
        if lis[i] % 2 == 0:
            eve.append(lis[i])
        i += 1
    return eve


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Given a list of number, varying the."""
    lis: list[int] = list()
    if len(a_list) == 0:
        return []
    if start < 0:
        start = 0
    if end > len(a_list): 
        end = len(a_list)
    while start < end: 
        lis.append(a_list[start])
        start += 1
    if len(a_list) == 0:
        start > len(a_list) or end <= 0
        lis.append(a_list[end])
    return lis


def concat(first: list[int], second: list[int]) -> list[int]:
    """Two list of integers combined."""
    done: list[int] = list()
    i: int = 0
    x: int = 0
    while i < len(first):
        done.append(first[i])
        i += 1
    while x < len(second):
        done.append(second[x])
        x += 1
    return done