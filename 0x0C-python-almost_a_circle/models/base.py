#!/usr/bin/python3
"""
Implementation of a base class for allother classes in this project. The goal
of it is to manage id attribute in all future classes to avoid duplicating
the same code (by extension, same bugs)
"""

import json
import os
import csv

class Base:

    """
     implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
