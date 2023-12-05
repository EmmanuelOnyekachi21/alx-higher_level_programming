#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = ()

    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]

    return first, second
