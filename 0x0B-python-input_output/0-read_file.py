#!/usr/bin/python3
"""This module pprovides functions for reading files"""


def read_file(filename=""):
    """
    Read the content of a text_file and print it to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None.
    """

    with open(filename, "r", encoding="UTF-8") as f:
        for lines in f:
            print(lines.strip())
