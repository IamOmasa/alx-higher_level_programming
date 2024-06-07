#!/usr/bin/python3
"""a function that returns a key with the biggest integer value"""


def best_score(a_dictionary):
    if not a_dictionary:
        return None

    a = list(a_dictionary.keys())
    b = sorted(list(a_dictionary.values()))

    b_index = b[len(a) - 1]
    b_name = None
    for key, value in a_dictionary.items():
        if value == b_index:
            b_name = key

    return b_name
