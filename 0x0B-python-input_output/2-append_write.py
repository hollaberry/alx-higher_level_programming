#!/usr/bin/python3
"""Module to append a string to the end of file"""


def append_write(filename="", text=""):
    """function to append s atring at the end of the text file"""

    with open(filename, 'a') as f:
        return f.write(text)
