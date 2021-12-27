#!/usr/bin/python3
"""Method that shows inheritance"""



class MyList(list):
    """Class Mylis inherits list"""

    def print_sorted(self):
        """Print list in a sorted form"""

        print(sorted(self))
