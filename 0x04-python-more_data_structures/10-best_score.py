#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:    # Check if the dictionary is empty or none
        return None

    max_score = max(a_dictionary.values())

    for key, value in a_dictionary.items():
        if value == max_score:
            return key

    return None     # Return None if no score is found
