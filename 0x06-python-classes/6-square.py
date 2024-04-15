#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines square by: (based on 5-square.py).
    Attributes:
         size: size of a square (1 side).
         area: returns the current square area.
    """

    def __init__(self, size=0, position=(0, 0)):
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
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    @property
    def position(self):
        """Return the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the new value of position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints in stdout the square with the character #"""
    for _ in range(position[1]):
        print("")

    if self.size == 0:
        print("")
    else:
        for i in range(self.size):
            print(" " * position[0] + "#" * self.size)
