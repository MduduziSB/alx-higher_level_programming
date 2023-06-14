#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = matrix.copy()
    for r in range(len(matrix)):
        n_matrix[r] = list(map(lambda y: y**2, matrix[r]))
    return n_matrix
