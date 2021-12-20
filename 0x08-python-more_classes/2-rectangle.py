#!/usr/bin/python3
"""Rectangle class that defines a rectangle"""

class Rectangle:
    """Represent a rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """initialise the attribute width and height"""
        self.width = width
        self.height = height


    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
        return(self.__width)


    @width.setter
    def width(self, value):
        """Sets the height of a Rectangle instance"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        
    @property
    def height(self):
        return(self.__height)
    
    @height.setter
    def height(self, value):
        """sets the height of a rectangle instance"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    """Create public instance method: area"""
    def area(self):
        return (self.__height * self.__width)

    """Create public instance method: perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))
