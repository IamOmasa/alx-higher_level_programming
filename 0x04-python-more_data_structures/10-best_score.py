#!/usr/bin/python3
"""a function that returns a key with the biggest integer value"""


def best_score(a_dictionary):
    a = list(a_dictionary.keys())
    b = sorted(list(a_dictionary.values()))
    b_name = b.index(b[len(b) - 1])

    if len(b) == 0:
        return ("None")

    return a[b_name]
