#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    if length > 0:
        for value in my_list[-1::-1]:
            print("{:d}".format(value))
