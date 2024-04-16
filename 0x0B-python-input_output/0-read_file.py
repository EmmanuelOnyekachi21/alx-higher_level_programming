#!/usr/bin/python3
"""0. Read file """


def read_file(filename=""):
    """Reads a text file and prints its content to stdout.

    Args:
        filename: The name of the file to read.  Defaults to an empty string.

    """
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
        print(contents, end="")
