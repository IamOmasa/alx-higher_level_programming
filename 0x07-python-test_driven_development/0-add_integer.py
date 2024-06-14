#!/usr/bin/python3
"""a function that adds 2 integers"""

def add_integer(a, b=98):
    """add integers
        args:
            a : int or float convert to int
            b : int or float convert to int
        Returns: int
    """
    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int,float)):
        raise TypeError("b must be an integer")
    return int (a) + int (b)
