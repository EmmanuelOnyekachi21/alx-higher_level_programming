#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    index = 0

    try:
        while printed_integers < x:
            if type(my_list[index]) == int:
                print("{:d}".format(my_list[index]), end="")
                printed_integers += 1
            index += 1
    except IndexError:
        pass

    print()
    return printed_integers
