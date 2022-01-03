#!/usr/bin/python3
"""Module to try JSON serialisation"""
import json


def to_json_string(my_obj):
    """function to return the JSON representation
    of an object by serialises obj to JSON formattes str"""

    return json.dumps(my_obj)
