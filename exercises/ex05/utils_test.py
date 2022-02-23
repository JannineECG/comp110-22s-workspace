"""Ex05 - utils test."""

__author__ = "730470181"

from utils import only_evens, sub, concat


def test_only_evens_many_items() -> None:
    """Testing only_evens."""
    eve: list[int] = [1, 2, 3, 4]
    assert only_evens(eve) == [2, 4]


def test_sub_many_items_2() -> None:
    """Testing sub."""
    lis: list[int] = [10, 20, 30, 40]
    assert sub(lis, 1, 3) == [20, 30]


def test_concat_single_item() -> None:
    """Testing concat."""
    done: list[int] = []
    assert concat(done, done) == []