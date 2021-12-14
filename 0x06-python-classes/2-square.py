#!/usr/bin/python3
"""Write a class square"""


class Square:
    """Represent a square"""


    def __init__(self, size=0):
        """initialise a private instance attribute to define a square
        Raise the type or value error exception according to given condition"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
