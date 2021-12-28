#!/usr/bin/python3
"""Module for inheriting a class from another class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialise an instance.
        with width and height as private"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """computes the area of rectangle """

        return self.__width * self.__height
