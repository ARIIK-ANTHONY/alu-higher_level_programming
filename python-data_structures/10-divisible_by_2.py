#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Check if numbers in a list are divisible by 2.

    This function takes a list of integers and returns a new list 
    where each element indicates whether the corresponding number 
    in the original list is divisible by 2 (True) or not (False).
    """
    return [num % 2 == 0 for num in my_list]
