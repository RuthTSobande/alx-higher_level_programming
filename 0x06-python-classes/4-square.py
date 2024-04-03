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
                Size is validated in the setter method.

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

    @property
    def size(self):
        """Method retrieves the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Method sets the size of a square.

        Args:
            size (int): Defines the size of the square.
                Size is validated with try/except.

        """
        try:
            self.__size = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """int: Returns area of square."""
        return self.__size * self.__size
