#!/usr/bin/python3
"""a function that replaces or adds key/value in a dictionary"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    
    for key, value in a_dictionary:
        print(f"{key}: {value}")
