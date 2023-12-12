#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = list()

    for row in matrix:
        new_row = list()
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)

    return new_matrix
