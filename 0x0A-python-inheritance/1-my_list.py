#!/usr/bin/python3
"""This contains a class definition which extends the list class
adding an instance method to produce a sorted replica of the list
"""


class MyList(list):
    """This class extends the list class

    it has an added instance method which prints the list in  sorted ascending
    format.
    """

    def print_sorted(self):
        """prints a sorted ascending format of the list."""
        # Create a copy of the list to avoid modifying the original
        sorted_list = self.copy()
        sorted_list.sort(key=int)
        print(sorted_list)
