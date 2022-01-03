#!/usr/bin/python3
"""Module save to json file"""


import json


def save_to_json_file(my_obj, filename):
    """function that write an object to a text file
    using a JSON representation"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
