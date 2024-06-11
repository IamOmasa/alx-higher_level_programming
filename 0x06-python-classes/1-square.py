#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    def __init__(self, size):
        """initilize a private instance size"""
        self.__size = size

    def get_size(self):
        """get the size of a the private square"""
        return self.__size

    def set_size(self, size):
        """set the size of the private square"""
        self.__size = size
