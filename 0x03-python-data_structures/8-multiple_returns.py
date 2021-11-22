#!/usr/bin/python3
def multiple_returns(sentence):
    str = ''.join(sentence)
    num = len(str)
    if num < 1:
        return None
    num = len(str) - 1
    return num
    return str[0]
