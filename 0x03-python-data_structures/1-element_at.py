#!/usr/bin/python3
def element_at(my_list, idx):
    num = len(my_list)
    num = num - 1
    if idx < 0 or idx > num:
        return None
return my_list[idx]
