#!/usr/bin/python3
"""a function that divides 2 integers and prints the result"""


def safe_print_division(a, b):
    try:
        result = a / b
        print("{:d} / {:d} : {}".format(a, b, result))

    except ZeroDivisionError:
        result = None
    finally:
        print("Inside results: {}".format(result))
