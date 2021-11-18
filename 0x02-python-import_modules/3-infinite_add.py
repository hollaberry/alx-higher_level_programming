#!/usr/bin/python3
if __name__ = __main__:
    import sys
    p = len(sys.argv)
    k = 0
    for i in range(1, p):
        k += int(sys.argv[i])
    print("{}".format(k))
