#!/usr/bin/python3
"""This module pprovides functions for reading files"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns number of characters written
    Args:
        filename (str): The name of the file to write to.
        text:   Text to be written

    Returns:
        bytes_written:  Number of bytes written.
    """

    with open(filename, "w", encoding="UTF-8") as f:
        bytes_written = f.write(text)
        return bytes_written
