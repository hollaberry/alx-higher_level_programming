#!/usr/bin/python3
def max_integer(my_list=[]):
    num = len(my_list)
    if num < 1:
        return "None"
    else:
        max = my_list[0]
        for i in range(num):
            if my_list[i] > max:
                max = my_list[i]
        return max
