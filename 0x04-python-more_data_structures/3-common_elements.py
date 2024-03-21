#!/usr/bin/python3
"""a function that returns a set of common elements in two sets"""


def common_elements(set_1, set_2):
    a = set(set_1)
    b = set(set_2)

    return a & b
