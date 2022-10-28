"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""

def lower_bound(x: list[int], v: int, low: int=0, high: bool=None) -> int:
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
    >>> lower_bound([2,3,5,5,7], 6)
    4
    >>> lower_bound([2,3,5,5,7], 4)
    2
    """
    high = high or len(x)
    if low >= high: return len(x) # if all elements in x are smaller than v. 
    mid = (low+high)//2 
    if mid == 0 and x[mid] >= v:
        return mid
    elif x[mid] >= v and x[mid-1] < v:
        return mid
    elif x[mid] > v:
        return lower_bound(x, v, low, mid)
    else: # x[mid] < v
        return lower_bound(x, v, mid+1, high)
    

def upper_bound(x: list[int], v: int, low: int=0, high: bool=None) -> int:
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
    if mid == 0 and x[mid] > v:
        return mid
    elif x[mid] > v and x[mid-1] <= v:
        return mid
    elif x[mid] > v:
        return upper_bound(x, v, low, mid)
    else: # x[mid] <= v
        return upper_bound(x, v, mid+1, high)
