#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None or len(my_list) == 0:
        return my_list

    new_m = []
    for x in my_list:
        if x == search:
            new_m.append(replace)
            continue
        new_m.append(x)
    return new_m
# Using list comprehension
# new_list = [x if x != search else replace for x in my_list]
