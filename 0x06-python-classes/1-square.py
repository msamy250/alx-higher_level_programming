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
            self.__size = size
