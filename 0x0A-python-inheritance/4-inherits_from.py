#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Function to check the kind of an object"""

    return isinstance(obj, a_class) and type(obj) != a_class
