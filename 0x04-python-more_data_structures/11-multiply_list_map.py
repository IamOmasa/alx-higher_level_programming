#!/usr/bin/python3
"""a function that returns a list with all values multiplied by a number"""


def multiply_list_map(my_list=[], number=0):
    from operator import mul
    return list(map(lambda x: x * number, my_list[:]))
