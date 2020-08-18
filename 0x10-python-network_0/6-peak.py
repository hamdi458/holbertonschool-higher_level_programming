#!/usr/bin/python3
"""find peak"""


def findpeak(list_of_integers, low, high, n): 
    """findpeak"""
       
    mid = low + (high - low)/2 
    mid = int(mid) 
      
  
    if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and 
        (mid == n - 1 or list_of_integers[mid + 1] <= list_of_integers[mid])): 
        return list_of_integers[mid] 
  
  
   
    elif (mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]): 
        return findpeak(list_of_integers, low, (mid - 1), n) 
  
    else: 
        return findpeak(list_of_integers, (mid + 1), high, n) 

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
