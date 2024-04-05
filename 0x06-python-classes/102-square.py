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
"""a square class"""


class Square:
    """Derives a square """
    def __init__(self, size=0):
        """Initializes the data
        Args:
            size (int): size of the square
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Raises:
            TypeError: when `size` isn't an integer
            ValueError: `size` is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def __lt__(self, other):
        """Compare less than of current instance and other instance"""
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare less than or equal to of current instance
        and other instance
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """Compare equality of current instance and other instance"""
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare not equal of current instance
        and other instance
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare greater than of current instance
        and other instance
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare greater than or equal to of current instance
        and other instance
        """
        return self.area() >= other.area()

    def area(self):
        """Calculates the area of a square
        Returns: the area of the square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves the value of `size`"""
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
        return self.__size

    @size.setter
    def size(self, value):
<<<<<<< HEAD
        """Set size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
=======
        """Sets the value of `value`
        Args:
            value (int): value to be set to `value`
        Raise:
            TypeError: when `value` isn't an integer
            ValueError: `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
            raise ValueError("size must be >= 0")

        self.__size = value
<<<<<<< HEAD

    def __le__(self, other):
        return self.size <= other.size

    def __lt__(self, other):
        return self.size < other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ne__(self, other):
        return self.size != other.size

    def __eq__(self, other):
        return self.size == other.size
=======
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
