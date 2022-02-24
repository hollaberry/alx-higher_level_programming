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

    @staticmethod

    def to_json_string(list_dictionaries):
        """ return the JSON string representation of list_dictionaries"""

        if list_dictionaries is not None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
            not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        if list_objs is None or list_objs == []:
           my_lstbj = "[]"
        else:
            my_lstbj = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(my_lstbj)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        m = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            m = json.loads(json_string)
        return m

     @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            - dictionary: used as **kwargs
        Returns: instance created
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    
