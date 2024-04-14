#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines square by: (based on 3-square.py).
    Attributes:
         size: size of a square (1 side).
         area: returns the current square area.
    """

    def __init__(self, size=0):
        """ Construct the class.
        Args:
            size: size of the square (1 side).
            """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square to new value with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
