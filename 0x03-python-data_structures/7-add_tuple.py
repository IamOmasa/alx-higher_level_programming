#!/usr/bin/python3
"""a function that adds 2 tuples"""


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    a, b = tuple_a(:2)
    c, d = tuple_b(:2)

    result = (a + c, b + d)

    return result
