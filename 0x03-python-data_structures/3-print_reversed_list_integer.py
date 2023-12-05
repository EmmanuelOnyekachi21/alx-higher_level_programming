#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    if length is None:
        return
    if length > 0:
        for i in range(length - 1, -1, -1):
            print("{}".format(my_list[i]), end='\n')
