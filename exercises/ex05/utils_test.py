"""Ex05 - utils test."""

__author__ = "730470181"

from utils import only_evens, sub, concat


def test_only_evens_none() -> None:
    """Testing only_evens for no int."""
    eve: list[int] = []
    assert only_evens(eve) == []


def test_only_evens_one_item() -> None:
    """Test only_evems for on int."""
    eve: list[int] = [2]
    assert only_evens(eve) == [2]
 

def test_only_evens_many_items() -> None:
    """Testing only_evens with multiple ints."""
    eve: list[int] = [1, 2, 3, 4]
    assert only_evens(eve) == [2, 4]


def test_sub_none() -> None:
    """Test sub for no list."""
    lis: list[int] = []
    assert sub(lis, 0, 0) == []


def test_sub_many_list_1() -> None:
    """Testing sub many list."""
    lis: list[int] = [10, 20, 30, 40]
    assert sub(lis, 1, 3) == [20, 30]


def test_sub_many_times2() -> None:
    """Testing sub in empty list."""
    lis: list[int] = [10, 20, 30, 40, 50, 60]
    assert sub(lis, 1, 4) == [20, 30, 40]


def test_concat_many_list() -> None:
    """Testing concat with many list."""
    done: list[int] = [60, 50]
    done2: list[int] = [1, 2, 5, 6]
    assert concat(done, done2) == [60, 50, 1, 2, 5, 6] 

    
def test_concat_no_list() -> None:
    """Testing concat no list."""
    done: list[int] = []
    assert concat(done, done) == []


def test_concat_one_int() -> None:
    """Testong concat with one int."""
    done: list[int] = [3]
    done2: list[int] = [1]
    assert concat(done, done2) == [3, 1]