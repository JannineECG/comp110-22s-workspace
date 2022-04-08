"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730470181"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here
    def __init__(self, values):
        """Initialize the values attributes of the newly constructed function."""
        self.values = values

    def __str__(self):
        """Creates an output of a list of str."""
        return f"Simpy({self.values})"

    def fill(self, num: float, times: int):
        """Allows us to print out a float an initialized values of times."""
        result: list[float] = []
        x: int = 0
        while x < times:
            result.append(num)
            x += 1
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Creates a list of arranged floats."""
        assert step != 0.0 
        result: list[float] = []
        while start > stop:
            result.append(start)  
            start += step
        while start < stop:
            result.append(start)
            start += step
        self.values = result

    def sum(self):
        """Adds up all the floats in the list.""" 
        return sum(self.values) 

    def __add__(self, lhs: Union[Simpy, float]):
        """Adds up either a float or another list of float from Simpy without mutating the orginal one."""
        result: list[float] = []
        if isinstance(lhs, float):
            for values in self.values:
                result.append(values + lhs)
        else:
            for i in range(0, len(self.values)):
                result.append(self.values[i] + lhs.values[i])
        
        return Simpy(result)

    def __pow__(self, lhs: Union[Simpy, float]):
        """Does exactly the same as the constructor __add__ except this one raises a float to a list of float or a list of float to another list of float."""
        result: list[float] = [] 
        if isinstance(lhs, float):
            for values in self.values:
                result.append(values ** lhs)
        else:
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** lhs.values[i])
        
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """This constructor checks to see if if two list[float] or a list[float] and float are similar."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for values in self.values:
                result.append(values == rhs)
        else:
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Much like the previous constructors, this one test if a certain list[float] is greater than anoter list[float] or float."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for values in self.values:
                result.append(values > rhs)
        else:
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """A better way to get an item that is being called for."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)
