#!/usr/bin/python3
"""a function that computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        for j in matrix[i]:
            new_matrix.append(j**2)

    return new_matrix
