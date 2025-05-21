"""
The functions for Lab 5

Initial skeleton by W. White (wmw2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


def lesser_than(alist, value):
    """
    Returns:  number of elements in alist strictly less than value
    
    Example:  lesser_than([5, 9, 1, 7], 6) evaluates to 2
    
    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list of ints
    
    Parameter value:  the value to compare to the list
    Precondition:  value is an int
    """
    # pass # Implement me
    return sum(1 for x in alist if x < value)


def uniques(alist):
    """
    Returns: The number of unique elements in the list. 
    
    Example: uniques([5, 9, 5, 7]) evaluates to 3
    Example: uniques([5, 5, 1, 'a', 5, 'a']) evaluates to 3
    
    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list.
    """
    # pass # Implement me
    return len(set(alist))

def clamp(alist, min, max):
    """
    Modifies the list so that every element is between min and max.
    
    Any number in the list less than min is replaced with min.  Any number
    in the list greater than max is replaced with max. Any number between
    min and max is left unchanged.
    
    This is a PROCEDURE. It modified alist, but does not return a new list.
    
    Example: if alist is [-1, 1, 3, 5], then clamp(thelist,0,4) changes
    alist to have [0,1,3,4] as its contents.
    
    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)
    
    Parameter min: the minimum value for the list
    Precondition: min <= max is a number
    
    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """
    # pass # Implement me
    for i in range(len(alist)):
        if alist[i] < min:
            alist[i] = min
        elif alist[i] > max:
            alist[i] = max