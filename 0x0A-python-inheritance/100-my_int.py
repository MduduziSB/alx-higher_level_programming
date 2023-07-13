#!/usr/bin/python3
"""
Defines a class that inerits from int
"""


class MyInt(int):
    """Definition of MyInt class"""
    def __eq__(self, other):
        """New definition of __eq__ method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """New definition of __nq__ method"""
        return super().__eq__(other)
