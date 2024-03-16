#!/usr/bin/python3
"""a function that replaces an element in a list at a specific position"""


def new_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)

    length = len(my_list)

    new_list = my_list[:]

    if 0 <= idx < length:
        new_list[idx] = element

    return(new_list)


