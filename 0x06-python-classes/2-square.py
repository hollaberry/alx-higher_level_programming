#!/usr/bin/python3
class Square:
    """creating of a class square"""
    def __init__(self, size=0):
        """creating an init method"""
        self.size = size
        try:
            print("{:d}".format(self.size))
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
