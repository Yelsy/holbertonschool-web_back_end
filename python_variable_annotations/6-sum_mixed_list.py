#!/usr/bin/env python3
""" function for calculating the sum of a list containing mixed """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the Sum of floats and ints"""
    return sum(mxd_lst)
