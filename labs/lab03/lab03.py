"""
Module for implementing Lab 03 functions.

This module uses the Time class provided by the module time.  It contains a single 
function: add_time.  You are requested to implement this function.

While you are encouraged to test your answers, you do not need to write  a unit test.  
Simply demonstrate your functions to you instructor to get get credit

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
import ctime

def add_time(time1, time2):
    """
    Returns: The sum of time1 and time2 as a new Time object
    
    Example: Sum of 1hr 59min and 1hr 2min is 3hr 1min 
    DO NOT ALTER time1 or time2, even though they are mutable
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    # pass # STUB. Implement me
    new_hours = time1.hours + time2.hours
    new_minutes = time1.minutes + time2.minutes
    if new_minutes >= 60:
        new_hours += 1
        new_minutes -= 60
    return ctime.Time(new_hours, new_minutes)