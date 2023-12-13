#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2

# Using List comprehension
#    uncommon_set = {element for element in set_1 if element not in set_2} | 
# {element for element in set_2 if element not in set_1}
