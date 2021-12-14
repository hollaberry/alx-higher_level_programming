#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        dum = fct(*args)
        return dum
    except Exception as en:
        print("Ëxception: {:s}".format(str(en)), file=sys.stderr)
        return None
