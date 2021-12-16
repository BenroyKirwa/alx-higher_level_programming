#!/usr/bin/python3
"""
Function that adds two integers
"""
def add_integer(a, b=98):
    """
    Function that adds two integers a,b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(a) in [float]:
        int(a)
    elif type(b) in [float]:
        int(b)

    return int(a + b)
