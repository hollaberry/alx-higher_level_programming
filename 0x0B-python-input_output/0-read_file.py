#!/usr/bin/python3
"""Module to read a text file UTF8 and prints it to stdout"""


def read_file(filename=""):
    """Function read_file """

    with open(filename) as f:
        data = f.read()
        print(data, end="")
