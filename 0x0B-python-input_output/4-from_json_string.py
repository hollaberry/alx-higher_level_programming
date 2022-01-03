#!/usr/bin/python3
"""Module from_json_string"""
import json


def from_json_string(my_str):
    """function that returns an object represented by a JSON string
    json.loads deserialises a string to a Python object"""

    return json.loads(my_str)
