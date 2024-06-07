"""a function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    multiple_of_two = {}
    for key, value in a_dictionary.items():
        multiple_of_two[key] = value * 2

    return multiple_of_two
