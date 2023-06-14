#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = [[0 for r in range(len(matrix))]
                      for c in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[i][j] = matrix[i][j]**2
        return new_matrix
    return None
