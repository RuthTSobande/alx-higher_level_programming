#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the square class"""


class Square:
    """Square class. Has a size"""
    def __init__(self, size=0):
        """Initialize Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Return size of the square"""
=======
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
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
        return self.__size

    @size.setter
    def size(self, value):
<<<<<<< HEAD
        """Set size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
=======
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
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
