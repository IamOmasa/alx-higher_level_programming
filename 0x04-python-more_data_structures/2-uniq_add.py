#!/usr/bin/python3
"""a function that adds all unique integers in a list
(only once for each integer)"""


def uniq_add(my_list=[]):
    uniq_elem = set()

    for i in my_list:
        uniq_elem.add(i)

    total = sum(uniq_elem)

    return total
