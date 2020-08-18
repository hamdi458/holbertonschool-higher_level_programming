#!/usr/bin/python3
"""find peak"""


def findpeak(ar, low, high, n):
    """findpeak"""

    mid = low + (high - low) / 2
    mid = int(mid)

    if ((mid == 0 or ar[mid - 1] <= ar[mid]) and
            (mid == n - 1 or ar[mid + 1] <= ar[mid])):
        return ar[mid]

    elif (mid > 0 and ar[mid - 1] > ar[mid]):
        return findpeak(ar, low, (mid - 1), n)

    else:
        return findpeak(ar, (mid + 1), high, n)


def find_peak(list_of_integers):
    """find_peak"""
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    return findpeak(list_of_integers, 0, n - 1, n)
