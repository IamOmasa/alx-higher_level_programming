#!/usr/bin/python3
"""a function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    mult_dict = {}
    for key, value in a_dictionary.items():
        mult_dict[key] = value * 2

    for key, value in mult_dict.items():
        print(f"{key}: {value}")

    return mult_dict
