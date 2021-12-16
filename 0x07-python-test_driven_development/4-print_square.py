#!/usr/bin/python3
"""
Function that prints a square with the character #
"""


def print_square(size):
    """
    Function that prints a square with the character # and must be > 0
    """

    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size < 0 and type(size) in [float]:
        raise TypeError("size must be an integer")
    for i in range(0,size):
        print ("#"*size)
