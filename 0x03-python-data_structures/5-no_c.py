#!/usr/bin/python3
"""a function that removes all characters c and C from a string"""


def no_c(my_string):
    str_length = len(my_string)

    i = 0
    no_c_string = my_string[:]

    for chr in range(str_length):
        if (my_string[char] == 'c' or my_string[char] == 'C'):
            no_c_string = no_c_string[:(char - i)] + my_string[(char + 1):]
            i += 1

    return (no_c_string)

