#!/usr/bing/python3
"""a function that raises a name exception with a message"""


def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError:
        raise
