#!/usr/bin/python3
"""
defining a rectangle class that inherits from base class
"""
from models.base import Base


class Rectangle(Base):
    """Implementation of a Rectangle class inheriting from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialisation
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y
