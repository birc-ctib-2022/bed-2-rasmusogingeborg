"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


from msvcrt import kbhit
import re


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.
    

    If all values in x are smaller than v, return len(x).
    >>> lower_bound([2,3,5,5,7], 1)
    0
    >>> lower_bound([2,3,5,5,7], 2)
    0
    >>> lower_bound([2,3,5,5,7], 5)
    2
    >>> lower_bound([2,3,5,5,7], 8)
    5
    """
    # FIXME: Obviously the answer isn't always 0
  

   

def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).
    >>> upper_bound([2,3,5,5,7], 1)
    0
    >>> upper_bound([2,3,5,5,7], 2)
    1
    >>> upper_bound([2,3,5,5,7], 5)
    4
    >>> upper_bound([2,3,5,5,7], 8)
    5
    """
    high = high or len(x)
    if low >= high: return len(x) # if all elements in x are smaller than v. 
    mid = (low+high)//2
    if x[mid] > v and x[mid-1] <= v:
        return mid
    elif x[mid] > v:
        return lower_bound(x, v, mid+1, high)
    else: # x[mid] == mid+2
        return lower_bound(x, v, low, mid)
