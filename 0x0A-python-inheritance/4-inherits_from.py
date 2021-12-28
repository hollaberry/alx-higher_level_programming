#!/usr/bin/python3
"""Module 4-inherits_from
finds if the object is an instance of a
class tha inherited (directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """Function to check the kind of an object"""

    return isinstance(obj, a_class) and type(obj) != a_class
