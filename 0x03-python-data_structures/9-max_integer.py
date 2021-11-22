#!/usr/bin/python3
def max_integer(my_list=[]):
    num = len(my_list)
    if num < 1:
        return none
    else:
        for i in range(num):
            if my_list[i] > my_list[i + 1]:
                return my_list[i]
            else:
                return my_list[i + 1]
