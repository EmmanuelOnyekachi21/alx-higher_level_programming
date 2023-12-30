#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    max_number = my_list[0]
    for value in my_list[1:]:   # Start loop from the second element
        if value > max_number:
            max_number = value

    return max_number
