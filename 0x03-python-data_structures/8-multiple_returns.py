#!/usr/bin/python3
"""a function that returns a tuple with the length of a string and
its first character"""


def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length < 1:
        return (None)
    else:
        return (length, first)
