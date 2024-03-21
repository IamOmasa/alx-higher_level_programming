#!/usr/bin/python3
"""a function that prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):

    sort_key = sorted(a_dictionary.keys())
    for key in sort_key:
        print(key ":", a_dictionary[key])
