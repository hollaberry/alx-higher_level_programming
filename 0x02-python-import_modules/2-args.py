#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    p = len(sys.argv)
    if p == 1:
        print("{} arguments.".format(p - 1))
    elif p == 2:
        print("{} argument:".format(p - 1))
    else:
        print("{} arguments:".format(p - 1))
    for i in range(1, p):
        print("{}: {}".format(p, sys.argv[i]))
