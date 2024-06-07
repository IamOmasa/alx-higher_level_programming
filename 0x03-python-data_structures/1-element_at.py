
"""function that retrieves an element from a list like in C"""


def element_at(my_list, idx):
    my_len = len(my_list)

    if idx < 0 or idx >= my_len:
        return None
    print(f"Element at index {idx} is {my_list[idx]}")
