#!/usr/bin/python3
"""This modules see the appending ability of its function"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file and returns
    the number of characters added.

    Args:
        filename: Name of file
        text: Data tok be written to the `filename`

    Returns:
        Bytes_written: the number of characters added.
    """
    with open(filename, "a", encoding="UTF-8") as file:
        bytes_written = file.write(text)

    return bytes_written
