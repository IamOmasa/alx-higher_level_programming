#!/usr/bin/python3
"""a module that defines a class Square"""


class Square:
    """a class Square that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """initilize a square instance


            Args:
                size (int): side of a square must be an integer >= 0
                position (tuple):  2 positive integers

            Raises:
                TypeError: position must be a tuple of 2 positive integers
                TypeError: if the value is not an int
                ValueError: if the value is < 0
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the Value of tuple position

            Args:
                value (int): value of positive tuple

            Return: value of positive tuple
        """
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """method to get area of square size

            Args:
            size (int): side of the square

            Return: square the value of the side of the sqaure (size)
        """

        return (self.__size) * (self.__size)

    def my_print(self):
        """method that print in stdout the square with character #

            Args:
                size : side of the square

                Return: square with character #
        """
        if self.__size == 0:
            print()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size)):

            print(" " * self.__position[0], end="")
            print("#" * (self.__size))
