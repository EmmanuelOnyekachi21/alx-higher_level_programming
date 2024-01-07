#!/usr/bin/python3
"""This is a module for matrix division"""


def matrix_divided(matrix, div):
    """
    matrix_divided divides all elements of a matrix.

    args:
        matrix: must be a list of lists of integers or floats
        div:  a number (integer or float) that is the divisor
    raises:
        TypeError: if Matrix is not list of lists of integers or floats.
                    Also if div is not a number
                    And if each row in the matrix is not equal
        ZeroDivisionError: If div == 0
    """
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    num_cols = len(matrix[0])
    for rows in matrix:
        if len(rows) != num_cols:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    for rows in matrix:
        new_row = []
        for cols in rows:
            result = round(cols / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
