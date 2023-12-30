#!/usr/bin/python3

def max_integer(my_list=[]):
    max_number = 0

    if len(my_list) == 0:
        return None

    for value in range(len(my_list)):
        if my_list[value] > max_number:
            max_number = my_list[value]

    return max_number
