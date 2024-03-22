#!/usr/bin/python3
"""a function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        a_dictionary[key] = a_dictionary.get(key) * 2

    for key, value in a_dictionary.items():
        print(f"{key}: {value}")
