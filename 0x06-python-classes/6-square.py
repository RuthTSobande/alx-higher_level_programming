#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the square class"""


class Square:
    """Square class. Has a size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) is not int or type(position[1]) is not int\
           or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Return size of the square"""
=======
"""A square class"""


class Square:
    """Derives a square """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data
        Args:
            size (int): size of the square
            position (tuple): two positive integers
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

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or not all(isinstance(v, int) for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
            raise ValueError("size must be >= 0")
=======
        """Sets the value of `size`
        Args:
            value (int): value to be set to `size`
        Raise:
            TypeError: when `value` isn't an integer
            ValueError: `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
        self.__size = value

    @property
    def position(self):
<<<<<<< HEAD
        """Return position of Square"""
=======
        """Retrieves `position` value """
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
        return self.__position

    @position.setter
    def position(self, value):
<<<<<<< HEAD
        """Set position of square"""
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or value[0] < 0 or value[1] < 0:
            raise TypeError(
                "position must be a tuple of two positive integers")
        self.__position = value

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            string = '#' * self.__size
            margin = ' ' * self.__position[0]
            for x in range(self.__size):
                print(margin, string, sep="")
=======
        """Sets the value of `position`
        Args:
            value (int): value to be set to `position` attribute
        Raise:
            TypeError: position isn't a tupple or doesn't contain 2
                       elements or has negative integers
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints a square to stdout using #"""
        if self.__size == 0:
            print()
            return

        [print() for i in range(self.position[1])]
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
