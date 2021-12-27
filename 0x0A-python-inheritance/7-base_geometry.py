#!/usr/bin/python3
"""Module for a class BaseGeometry"""

class BaseGeometry:
    """Empty class"""
    pass

def area(self):
    """Function to rasie an exception"""
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """Function to set value"""
    if type(value) is not int:
        raise TypeError("{} must be greater than 0".format(name))

    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
        
