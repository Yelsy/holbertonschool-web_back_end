#!/usr/bin/env python3
""" function to create tuples with a string
and the square of an integer or float value."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple"""
    return k, pow(v, 2)
