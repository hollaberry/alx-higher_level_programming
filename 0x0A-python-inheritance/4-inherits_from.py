#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Function to check the kind of an object"""

    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
