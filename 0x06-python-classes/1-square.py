#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    def __init__(self, size):
        """initilize a private instance size"""
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size
