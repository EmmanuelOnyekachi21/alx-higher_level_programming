#!/usr/bin/python3
"""This is a "Say my name" module"""

def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>

    args:
        first_name: This is the first_name of a person
        last_name: This is the last name of a person

    raises:
        TypeError: if lastname or firstname is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
