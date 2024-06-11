#!/usr/bin/python3
"""a module that defines a class Square"""


class Square:
    """a class Square that defines a square """
    def __init__(self, size=0):
        """initilize a square instance


            Args:
                size (int): side of a square must be an integer >= 0

            Raises:
                TypeError: if the value is not an int
                ValueError: if the value is < 0
        """

        self.size = size

    @property
    def size(self):
        """Retrieve the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the square

            Args:
                value (int): defined value of size

            Return: value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method to get area of square size

            Args:
            size (int): side of the square

            Return: square the value of the side of the sqaure (size)
        """

        return int(self.__size) * int(self.__size)
