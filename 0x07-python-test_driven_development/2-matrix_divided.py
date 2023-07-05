#!/usr/bin/python3
"""matrix division module"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""

    for idx in range(len(matrix)):
        for idy in range(len(matrix[idx])):
            if (type(matrix[idx][idy]) != int and
                    type(matrix[idx][idy]) != float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    for idx in range(1, len(matrix)):
        if len(matrix[idx]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    n_matrix = matrix.copy()
    for r in range(len(matrix)):
        n_matrix[r] = list(map(lambda y: round(y/float(div), 2), matrix[r]))
    return n_matrix
