#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        n = fct(*args)
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        return None
    return n
