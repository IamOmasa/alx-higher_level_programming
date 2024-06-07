#!/usr/python3
"""function that retrieves an element from a list like in C"""


def element_at(my_list, idx):
    my_len = len(my_list)

    if idx < 0 or idx > (my_len - 1):
        return (None)
    else:
        print(f"Element at index {idx} is {my_list[idx]}")
