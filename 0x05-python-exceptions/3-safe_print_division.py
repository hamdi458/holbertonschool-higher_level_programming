#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        nb = a / b
    except ZeroDivisionError:
        nb = None
    finally:
        print("Inside result: {}".format(nb))
    return nb
