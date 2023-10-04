#!/usr/bin/env python3
"""Module that returns list of random floating-point numbers"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns the list of random floating-point numbers."""
    list_random = [x async for x in async_generator()]
    return list_random
