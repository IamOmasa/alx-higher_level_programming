#!/usr/bin/python3
"""a function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    a_dictionary.update((x, y * 2) for x, y in a_dictionary.items())

    for key, value in a_dictionary.items():
        print(f"{key}: {value}")
