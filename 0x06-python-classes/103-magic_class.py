#!/usr/bin/python3
<<<<<<< HEAD
=======
"""Magic class from a given ByteCode."""
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
import math


class MagicClass:
<<<<<<< HEAD
    """A circle class"""

    def __init__(self, radius=0):
        """Initialized circle"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return circumference of circle"""
        return 2 * math.pi * self.__radius
=======
    """Initialize the MagicClass"""
    def __init__(self, radius=0):
        """Initializes the data"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculates the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference"""
        return 2 * math.pi * self._MagicClass__radius
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
