#!/usr/bin/python3
"""a function that adds all unique integers in a list
(only once for each integer)"""


def uniq_add(my_list=[]):
    uniq_elem = []

    sum = 0
    for i in my_list:
        if i != i+1:
            uniq_elem.append(i)

    for j in uniq_elem:
        sum += j

    return sum
