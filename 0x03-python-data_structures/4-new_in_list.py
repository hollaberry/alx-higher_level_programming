#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    num = len(my_list)
    num = num - 1
    new_list = my_list.copy()
    if idx < 0 or idx > num:
        return my_list.copy()
    else:
        new_list[idx] = element
        return new_list
    
