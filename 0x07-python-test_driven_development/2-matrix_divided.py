#!/usr/bin/python3
"""
    This module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function to divide all elements of a matrix

    Args:
        matrix (list of lists): list of lists of integers or floats
        div (int): integer > 0 used to divide each element of matrix
    Raises:
        TypeError: If matrix is not a list of lists
        TypeError: If each row of matrix is not same size
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div is = 0
    Return:
        A new matrix
    Note:
        Each element of the matrix will be rounded to 2 d.p. after division
    """

    for row in matrix:
        size = len(matrix[0])
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(row)):
            if type(row[i]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = [[round((i/div), 2) for i in row] for row in matrix]
    return res
