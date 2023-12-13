#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = list()
    uniq_add = 0

    for num in my_list:
        if num in unique:
            continue
        uniq_add += num
        unique.append(num)
    return uniq_add
