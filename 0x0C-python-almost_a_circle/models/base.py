#!/usr/bin/python3
"""Base model"""

class Base:
    """Class that defines properties of square.
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Construct the class.
        Args:
            id: id of the object.
        """
        if id is not None :
            self.id = id
        else :
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
