#!/usr/bin/python3
""" function that finds the peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    highest = 0
    for number in list_of_integers:
        if number > highest:
            highest = number
    return highest

            
