#!/usr/bin/python3
"""This module has a class `MyInt` inheriting from class `int`
"""
class MyInt(int):
    """MyInt class inherits from int but inverts the behavior of == and !=."""
    def __eq__(self, other):
        """Overrides the == operator to return the opposite of the original comparison."""
        return not super().__eq__(other)
    def __ne__(self, other):
        """Overrides the != opertor to return the opposite of the original comparison."""
        return not super().__ne__(other)
