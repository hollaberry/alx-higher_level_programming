#!/usr/bin/python3
"""Module class student"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a student instance"""
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            d = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    d[k] = v
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for (key, value) in json.items():
            setattr(self, key, value)
