#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """Class defines a square.

    Class has no public attributes.

    """
    def __init__(self, size=0):
        """Method initiates a square.

        Args:
            size (int): Defines the size of the square.
                Size is validated with try/except.

        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """int: Return area of square."""
        return self.__size * self.__size
