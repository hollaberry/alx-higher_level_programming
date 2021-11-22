#!/usr/bin/python3
def no_c(my_string):
    final_username = my_string.translate({ ord(c): None for c in "cC"})
    return final_username
