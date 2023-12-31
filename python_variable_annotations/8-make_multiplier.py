#!/usr/bin/env python3
""" function  that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier function"""
    def multiplier_function(x: float) -> float:
        """return the multiplier function by multiplier"""
        return multiplier * x

    return multiplier_function
