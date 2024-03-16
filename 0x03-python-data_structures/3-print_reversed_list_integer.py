#!/usr/bin/python3
"""a function that prints all integers of a list, in reverse order"""


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        indx = len(mylist) - 1

        while indx >= 0:
            print("{:d}".format(my_list[indx]))
            indx -= 1
