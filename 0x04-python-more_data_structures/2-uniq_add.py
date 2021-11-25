#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = sorted(my_list)
    total = 0
    for i in new_list:
        if new_list[i] != new_list[i - 1]:
            total += new_list[i]
    return total
