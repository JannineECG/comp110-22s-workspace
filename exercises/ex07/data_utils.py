"""Dictionary related utility functions."""

__author__ = "730470181"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    end: list[str] = []
    for row in table: 
        item: str = row[column]
        end.append(item)
    return end


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(cols: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Create a column-based table with the fist N row of data for each column."""
    end: dict[str, list[str]] = {}
    for key in cols:
        xs: list[str] = []
        i: int = 0
        while i <= N:
            xs.append(cols[key][i])
            i += 1
        end[key] = xs
    return end


def select(cols: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Selecting columns you only want."""
    end: dict[str, list[str]] = {}
    for key in name:
        end[key] = cols[key]
    return end


def concat(col_1: dict[str, list[str]], col_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """5 stops from March 21st and 5 stops from March 27th."""
    end: dict[str, list[str]] = {}
    for key in col_1:
        end[key] = col_1[key]
    for key in col_2:
        if col_2 in end[key]:
            col_2[key] += end
        else:
            end[key] = col_2[key]
    return end


def count(fre: list[str]) -> dict[str, int]:
    """The sex and race of all the people stopped."""
    end: dict[str, int] = {}
    for key in fre:
        if key in end:
            end[key] += 1
        else:
            end[key] = 1
    return end