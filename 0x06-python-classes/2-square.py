#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).
    Attribuites : 
        Size : is a size of one side in square (1 side)
    """
    def __init__(self, size):
            """constructe the class
            Args:
                Size: size of the square.
            """
    def size(self, value):
        """ Set the size of the square 
        Args:
        Value (int) = New size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
            self.__size = size
