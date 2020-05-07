#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    x = tuple_a + ('0', '0')
    y = tuple_b + ('0', '0')

    somme1 = int(x[0]) + int(y[0])
    somme2 = int(x[1]) + int(y[1])
    return(somme1), (somme2)
