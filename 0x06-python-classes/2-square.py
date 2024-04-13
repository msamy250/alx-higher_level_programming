#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """
    Class that defines properties of a square (based on 0-square.py).
    Attributes:
        size (int): Size of one side of the square.
    """
    def __init__(self, size=0):
            """ Construct the class.
        Args:
            size (int): Initial size of the square.
            """
        self.__size = size
    
    @property
    def size(self):
        """
        Get the size of the square.
        Returns:
            int: The current size of the square.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """ Set the size of the square.
        Args:
            value (int): New size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
