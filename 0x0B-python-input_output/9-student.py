#!/usr/bin/python3
"""Module class student"""


class student:
    """student"""
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        """to_json"""
        return self.__dict__
