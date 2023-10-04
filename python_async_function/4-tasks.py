#!/usr/bin/env python3
"""script async python"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """scritp to return list of delays in ascending order"""
    many_delays = [
        task_wait_random(max_delay) for o in range(n)
    ]
    Results = []
    for i in asyncio.as_completed(many_delays):
        result = await i
        Results.append(result)
    return Results
