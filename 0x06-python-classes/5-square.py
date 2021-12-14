#!/usr/bin/python3
"""Write a class Square"""
   import sys



class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """ Initialize the attribute : size"""
        self.size = size

    """Getter"""
    @property
    def size(self):
        return (self.__size)

    """Setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Create public instance method: def area(self)"""
    def area(self):
        sq_area = self.__size ** 2
        return (sq_area)

    """Create public instance method: my_print
    prints square with # character"""

    def my_print(self):
        if self.__size == 0:
        new_value = self.__size)
        for i in range(new_value):
            print("#" * self.__size)
