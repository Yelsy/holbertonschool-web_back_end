#!/usr/bin/env python3
""" Script that returns the list of all delays in ascending order"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ function that returns a list of floating random numbers n times
    in ascending order"""
    list_delays = [wait_random(max_delay) for _ in range(n)]

    delays = [await i for i in asyncio.as_completed(list_delays)]

    sorted_list = sorted(delays)
    return sorted_list
