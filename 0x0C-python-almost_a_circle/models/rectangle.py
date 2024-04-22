#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base

class Rectangle(Base):
    """Class that defines properties of rectangle.
    """

    def __init__(self, width, height, x = 0, y = 0, id = None):
        """Construct the class.
        Args:
            width: width of the rectangle.
            height: height of the rectangle.
            x: x position of the rectangle.
            y: y position of the rectangle.
            id: id of the object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of rectangle to new value with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of rectangle to new value with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Returns the x position of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x position of rectangle to new value with validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the y position of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y position of rectangle to new value with validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the rectangle with the character #.
        """
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
