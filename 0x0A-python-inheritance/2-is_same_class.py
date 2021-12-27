#!/usr/bin/python3
"""Module to check for an instance"""

def is_same_class(obj, a_class):
    """function to check fo ran instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
