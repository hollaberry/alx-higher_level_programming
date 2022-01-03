#!/usr/bin/python3
"""Module load json"""
import json


def load_from_json_file(filename):
    """function that create an object from
    a JSON file"""

    with open(filename) as f:
        return json.load(f)
