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

    def __repr__(self):
        retstr = ""
        if self.__size == 0:
            pass
        else:
            for x in range(self.__position[1]):
                retstr += '\n'
            string = '#' * self.__size
            margin = ' ' * self.__position[0]
            retstr += margin + string
            for x in range(1, self.__size):
                retstr += '\n' + margin + string
        return retstr

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Return size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return position of Square"""
        return self.__position

    @position.setter
    def position(self, value):
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
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise a new square.
        Args:
            size (int): Size of the new square.
            position (int, int): Position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Defines the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
