#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for char in my_string:
        if ord(char) == ord('c') or ord(char) == ord('C'):
            continue
        new_str += char
    return new_str
