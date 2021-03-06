#!/usr/bin/python3
"""Module for inheriting a class from another class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inheriting from Rectangle"""

    def __init__(self, size):
        """Initialise an instance.
        with width and height as private"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """Area method implementation"""

        return self.__size ** 2
