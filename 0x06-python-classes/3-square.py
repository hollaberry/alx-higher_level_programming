#!/usr/bin/python3
"""Write a class square"""

class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """initialise the private  instance attribute: size
        Raise the TypeError or ValueError according to given condition"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    """Create public instance method: def area(self)"""
    def area(self):
        return(self.__size ** 2)
    
