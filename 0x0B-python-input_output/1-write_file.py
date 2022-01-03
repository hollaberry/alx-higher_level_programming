#!/usr/bin/python3
"""Module to write another file to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
    Returns the number of characters written"""

    with open(filename, 'w') as f:
        return f.write(text)
