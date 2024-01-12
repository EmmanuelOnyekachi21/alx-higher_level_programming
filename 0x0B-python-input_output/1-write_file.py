#!/usr/bin/python3
"""This module provides functions used for writing to a file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number of characters
    written:

    Args:
        filename: NAme of file
        text: Data to be written
    Returns:
        bytes_written: The number of characters written
    """

    with open(filename, "w", encoding="UTF-8") as file:
        data_written = file.write(text)
    return data_written
