#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    high_key = list(a_dictionary.keys())[0]
    max = a_dictionary[high_key]
    for k, v in a_dictionary.items():
        if v > max:
            high_key = k
            max = v
    return high_key
