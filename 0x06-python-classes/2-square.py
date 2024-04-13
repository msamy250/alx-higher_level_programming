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
    
if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
