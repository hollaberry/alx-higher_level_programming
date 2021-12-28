#!/usr/bin/python3
"""Module to create class MTINT"""


class MyInt(int):
    """Class inheriting from int,
    But reverses the behaviou of != and ==.
    """

    def __eq__(self, other):
        """Opposing the equality."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Ïnequality becomes equality."""

        return super().__eq__(other)
