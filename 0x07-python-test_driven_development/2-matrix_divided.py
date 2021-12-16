#!/usr/bin/python3
"""
Function that divides all element of a matrix
"""
def matrix_divided(matrix, div):


    """
    Function that divides all elements of a matrix
    """
    for y in matrix:
        if not y or not isinstance(y, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for num in y:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    total_length = sum(len(row) for row in matrix)
    if total_length % 2 != 0 and total_length != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    x = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return x
