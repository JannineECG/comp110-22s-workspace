"""Testing EX06 - Dictionary Functions."""

__author__ = "730470181"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_none() -> None:
    """Invert keyerror."""
    with pytest.raises(KeyError):
        a = {'kris': 'jordan', 'michael': 'jordan'}
        invert(a)


def test_invert_one() -> None:
    """Testing invert for one dictionary."""
    result: dict[str, str] = {'a': 'z'}
    assert invert(result) == {'z': 'a'}


def test_invert_two() -> None:
    """Testing invert for multiple dictionaries."""
    result: dict[str, str] = {'a': 'z', 'y': 'b'}
    assert invert(result) == {'z': 'a', 'b': 'y'}


def test_favorite_color_none() -> None:
    """Testing favorite color with none the same."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "pink"}
    assert favorite_color(colors) == ('yellow')


def test_favorite_color_multiple() -> None:
    """Testing favorite color with multiple the same."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == ("blue")


def test_favorite_color_all_same() -> None:
    """Testing favorite color with all the same."""
    colors: dict[str, str] = {"Marc": "pink", "Ezri": "pink", "Kris": "pink"}
    assert favorite_color(colors) == ("pink")


def test_count_none() -> None:
    """Testing count for no similar dictionaries."""
    val: list[str] = ["hi", "no", "bye"]
    assert count(val) == {'bye': 1, 'hi': 1, 'no': 1}


def test_count_all() -> None:
    """Testing count for all similar dictionaries."""
    val: list[str] = ["hi", "hi", "hi"]
    assert count(val) == {'hi': 3}


def test_count_2() -> None:
    """Testig count for two sets of similar dictionaries."""
    val: list[str] = ["hi", "hi", "bye", "bye"]
    assert count(val) == {'hi': 2, 'bye': 2}
 