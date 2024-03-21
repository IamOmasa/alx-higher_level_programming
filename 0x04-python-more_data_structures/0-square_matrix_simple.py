#!/usr/bin/python3
"""a function that computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        sq_row = []
        for j in i:
            sq_row.append(j**2)
        new_matrix.append(sq_row)

    return new_matrix
