#!/usr/bin/python3
"""
This Module creates a class `MyList` that inherits from the Base class `list`
"""


class MyList(list):
    """
    This class inherits from the Base class `list`

    Public Instance Method:
        print_sorted(self): that prints the list, but sorted (ascending sort)

    """
    def print_sorted(self):
        """
        This class prints the list, but sorted in asceding order.
        """
        print(sorted(self))
